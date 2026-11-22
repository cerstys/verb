#!/bin/zsh
# Прыжок FAQ на закрытии: каждый вопрос — открыть, закрыть, высота по кадрам; печатает наибольший шаг последнего кадра (px).
# zsh design/instrumenty/faq-zamer.sh <файл.html> …
cd "${0:A:h}/../.."
J="(async()=>{const s=ms=>new Promise(r=>setTimeout(r,ms));const out=[];for(const d of document.querySelectorAll('.faq details')){d.scrollIntoView({block:'center'});await s(80);d.querySelector('summary').click();await s(500);const h=[];d.querySelector('summary').click();const t0=performance.now();while(performance.now()-t0<520){h.push(d.getBoundingClientRect().height);await new Promise(r=>requestAnimationFrame(r))}h.push(d.getBoundingClientRect().height);const st=h.filter((v,i,a)=>i==0||Math.abs(v-a[i-1])>.01);out.push(+(st.at(-2)-st.at(-1)).toFixed(1))}return out.join(' ')})()"
for f in "$@"; do for w in 1440 375; do print -n "$f $w: "; node design/instrumenty/cdp.mjs js "file://$PWD/$f" $w 900 design/shots/faq/x.jpg "$J" 1 2>&1 | tr -d '"'; done; done
