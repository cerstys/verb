// Замер кадров и съёмка черновиков через headless Chrome (CDP), без зависимостей (Node 22+: встроенный WebSocket).
// node design/instrumenty/cdp.mjs fps  <url> <ширина> [замедление ЦП, 1|4]   → время кадра при плавной прокрутке
// node design/instrumenty/cdp.mjs shot <url> <ширина> <высота> <выход.jpg> <прокрутка: px | "p0.5" (доля страницы) | "#селектор"> [масштаб] [ждать мс]
// node design/instrumenty/cdp.mjs el <url> <ширина> <высота> <выход.png> <селектор> <масштаб> [ждать]  → снимок элемента (RM=1 — reduced motion, DARK=1 — ночь)
// node design/instrumenty/cdp.mjs js <url> <ширина> <высота> <выход.jpg> <выражение JS (может быть промисом)> [масштаб] → выполнить сценарий на странице и снять экран
// node design/instrumenty/cdp.mjs frames <url> <ширина> <высота> <папка> <кадров> <мс между> <прокрутка>  → серия кадров по времени (для видео)
import { spawn } from 'node:child_process';
import { writeFileSync, mkdtempSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const [, , mode, url, ...a] = process.argv;
const port = 9300 + Math.floor(Math.random() * 500);
const prof = mkdtempSync(join(tmpdir(), 'cdp-'));
const ch = spawn(CHROME, ['--headless=new', `--remote-debugging-port=${port}`, `--user-data-dir=${prof}`, '--hide-scrollbars',
  '--no-first-run', '--force-color-profile=srgb', 'about:blank'], { stdio: 'ignore' });
const sleep = ms => new Promise(r => setTimeout(r, ms));

let ws, id = 0, traceEv = [], traceDone; const wait = new Map();
async function connect() {
  for (let i = 0; i < 50; i++) {
    try { const l = await (await fetch(`http://127.0.0.1:${port}/json`)).json(); const p = l.find(t => t.type === 'page'); if (p) { ws = new WebSocket(p.webSocketDebuggerUrl); break } } catch { }
    await sleep(200);
  }
  await new Promise(r => ws.onopen = r);
  ws.onmessage = e => { const m = JSON.parse(e.data); if (m.id && wait.has(m.id)) { wait.get(m.id)(m); wait.delete(m.id) }
    else if (m.method === 'Tracing.dataCollected') traceEv.push(...m.params.value); else if (m.method === 'Tracing.tracingComplete') traceDone && traceDone() };
}
const cmd = (method, params = {}) => new Promise((res, rej) => { const i = ++id; wait.set(i, m => m.error ? rej(new Error(method + ': ' + m.error.message)) : res(m.result)); ws.send(JSON.stringify({ id: i, method, params })) });
const ev = async expr => (await cmd('Runtime.evaluate', { expression: expr, awaitPromise: true, returnByValue: true })).result.value;

async function open(w, h, scale = 1) {
  await cmd('Page.enable');
  if (process.env.RM) await cmd('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: 'reduce' }] });
  if (process.env.DARK) await cmd('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-color-scheme', value: 'dark' }] });
  await cmd('Emulation.setDeviceMetricsOverride', { width: w, height: h, deviceScaleFactor: scale, mobile: w < 600 });
  if (process.env.CSS) await cmd('Page.addScriptToEvaluateOnNewDocument', { source: `addEventListener('DOMContentLoaded',()=>{const s=document.createElement('style');s.textContent=${JSON.stringify(process.env.CSS)};document.head.append(s)})` });
  await cmd('Page.navigate', { url });
  await sleep(600); await ev('document.fonts.ready.then(()=>1)'); await sleep(900);
}
async function scrollTo(s) {
  const y = s.startsWith('#') || s.startsWith('.') ? `document.querySelector('${s}').getBoundingClientRect().top+scrollY-80`
    : s.startsWith('p') ? `(document.documentElement.scrollHeight-innerHeight)*${s.slice(1)}` : s;
  await ev(`scrollTo(0,${y});dispatchEvent(new Event('scroll'));1`);
}

try {
  await connect();
  if (mode === 'trace') {   // trace <url> <ширина> [замедление ЦП] → мс работы главного потока и растра за прокрутку вниз-вверх, по видам
    const w = +a[0], h = w < 600 ? 812 : 900, slow = +(a[1] || 1);
    await open(w, h);
    if (slow > 1) await cmd('Emulation.setCPUThrottlingRate', { rate: slow });
    await cmd('Tracing.start', { categories: 'devtools.timeline,disabled-by-default-devtools.timeline.frame,cc', transferMode: 'ReportEvents' });
    const H = await ev('document.documentElement.scrollHeight-innerHeight');
    const t0 = Date.now();
    await cmd('Input.synthesizeScrollGesture', { x: w / 2, y: h / 2, yDistance: -H, speed: 1600, gestureSourceType: 'touch' });
    await cmd('Input.synthesizeScrollGesture', { x: w / 2, y: h / 2, yDistance: H, speed: 1600, gestureSourceType: 'touch' });
    const secs = (Date.now() - t0) / 1000;
    const done = new Promise(r => traceDone = r); await cmd('Tracing.end'); await done;
    const want = { Paint: 'paint', RasterTask: 'raster', PaintImage: 'paint', UpdateLayoutTree: 'style', Layout: 'layout', 'Decode Image': 'decode', ImageDecodeTask: 'decode', FunctionCall: 'script', EvaluateScript: 'script', FireAnimationFrame: 'script' };
    const sum = {}; let paints = 0, dropped = 0;
    for (const e of traceEv) { const k = want[e.name]; if (k && e.ph === 'X' && e.dur) sum[k] = (sum[k] || 0) + e.dur / 1000; if (e.name === 'Paint') paints++; if (e.name === 'DroppedFrame' || e.name === 'Frame Dropped') dropped++ }
    for (const k in sum) sum[k] = +sum[k].toFixed(1);
    console.log(JSON.stringify({ url, width: w, cpuSlowdown: slow, scrollSeconds: +secs.toFixed(1), msPerKind: sum, paintEvents: paints, droppedFrames: dropped }));
  } else if (mode === 'fps') {
    const w = +a[0], h = w < 600 ? 812 : 900, slow = +(a[1] || 1);
    await open(w, h);
    if (slow > 1) await cmd('Emulation.setCPUThrottlingRate', { rate: slow });
    await ev(`window.__f=[];(function f(t){__f.push(t);requestAnimationFrame(f)})(performance.now());1`);
    const H = await ev('document.documentElement.scrollHeight-innerHeight');
    // плавная прокрутка жестом, как пальцем/колесом: вниз до конца и обратно
    await cmd('Input.synthesizeScrollGesture', { x: w / 2, y: h / 2, yDistance: -H, speed: 1600, gestureSourceType: 'touch', repeatCount: 1 });
    await cmd('Input.synthesizeScrollGesture', { x: w / 2, y: h / 2, yDistance: H, speed: 1600, gestureSourceType: 'touch', repeatCount: 1 });
    const f = await ev('__f'); const d = f.slice(1).map((t, i) => t - f[i]).filter(x => x > 0).sort((x, y) => x - y);
    const q = p => d[Math.min(d.length - 1, Math.floor(d.length * p))];
    const long = d.filter(x => x > 25).length, sum = d.reduce((s, x) => s + x, 0);
    console.log(JSON.stringify({ url, width: w, cpuSlowdown: slow, frames: d.length, fps: +(1000 * d.length / sum).toFixed(1),
      medianMs: +q(.5).toFixed(1), p95Ms: +q(.95).toFixed(1), maxMs: +d[d.length - 1].toFixed(1), longFramesOver25ms: long }));
  } else if (mode === 'shot') {
    const [w, h, out, s = '0', sc = '1', ms = '1200'] = a;
    await open(+w, +h, +sc); await scrollTo(s); await sleep(+ms);
    const r = await cmd('Page.captureScreenshot', { format: 'jpeg', quality: 86 });
    writeFileSync(out, Buffer.from(r.data, 'base64')); console.log(out);
  } else if (mode === 'el') {   // el <url> <ширина> <высота> <выход> <селектор> <масштаб> [ждать мс]
    const [w, h, out, sel, sc = '2', ms = '800'] = a;
    await open(+w, +h, +sc); await scrollTo(sel); await sleep(+ms);
    const r0 = await ev(`(()=>{const r=document.querySelector('${sel}').getBoundingClientRect();return [r.left+scrollX,r.top+scrollY,r.width,r.height]})()`);
    const r = await cmd('Page.captureScreenshot', { format: 'png', captureBeyondViewport: true, clip: { x: r0[0], y: r0[1], width: r0[2], height: r0[3], scale: 1 } });
    writeFileSync(out, Buffer.from(r.data, 'base64')); console.log(out, r0);
  } else if (mode === 'scrub') {   // scrub <url> <ширина> <высота> <папка> <кадров> <от> <до> [мс между]; от/до: px | p0.3 (доля страницы) | .селектор@доляОкна
    const [w, h, dir, n, from, to, gap = '120'] = a;
    await open(+w, +h);
    const at = async v => v.startsWith('p') ? await ev(`(document.documentElement.scrollHeight-innerHeight)*${v.slice(1)}`)
      : /^[.#]/.test(v) ? await ev(`document.querySelector('${v.split('@')[0]}').getBoundingClientRect().top+scrollY-innerHeight*${v.split('@')[1] || .5}`) : +v;
    const y0 = await at(from), y1 = await at(to);
    for (let i = 0; i < +n; i++) {
      await ev(`scrollTo(0,${y0 + (y1 - y0) * i / (+n - 1)});1`); await sleep(+gap);
      const r = await cmd('Page.captureScreenshot', { format: 'jpeg', quality: 80 });
      writeFileSync(join(dir, String(i).padStart(3, '0') + '.jpg'), Buffer.from(r.data, 'base64'));
    }
    console.log(dir, y0, y1);
  } else if (mode === 'js') {
    const [w, h, out, expr, sc = '1'] = a;
    await open(+w, +h, +sc); const val = await ev(expr);
    const r = await cmd('Page.captureScreenshot', { format: 'jpeg', quality: 92 });
    writeFileSync(out, Buffer.from(r.data, 'base64')); console.log(JSON.stringify(val));
  } else if (mode === 'frames') {
    const [w, h, dir, n, gap, s = '0'] = a;
    await open(+w, +h); await scrollTo(s);
    for (let i = 0; i < +n; i++) {
      const r = await cmd('Page.captureScreenshot', { format: 'jpeg', quality: 80 });
      writeFileSync(join(dir, String(i).padStart(3, '0') + '.jpg'), Buffer.from(r.data, 'base64')); await sleep(+gap);
    }
    console.log(dir);
  }
} finally { ch.kill(); }
process.exit(0);
