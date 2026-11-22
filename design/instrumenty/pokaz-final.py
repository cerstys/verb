# Показ финала владельцу одним файлом: кадры финала (вшиты), превью для соцсетей, что добавлено. → design/pokaz-E9/final.html
import base64, html, json, re
O = 'design/shots/final-E9'
img = lambda p, w='100%': f'<img src="data:image/jpeg;base64,{base64.b64encode(open(p,"rb").read()).decode()}" style="width:{w};border:1px solid #ccd;border-radius:8px" loading="lazy">'
def ld(f): return json.loads(re.search(r'ld\+json">(.*?)</script>', open(f).read())[1])
rows = ''
for lang, name in (('ru', 'RU · docs/index.html'), ('en', 'EN · docs/en.html')):
    rows += f'<h2>{name}</h2><div class=g4>' + ''.join(
        f'<figure>{img(f"{O}/{lang}-{w}-{t}-{p}-final.jpg")}<figcaption>{w} · {"день" if t=="den" else "ночь"} · {p}</figcaption></figure>'
        for w, p in (('1440', 'p0'), ('375', 'p0.4')) for t in ('den', 'noch')) + '</div>'
faq = ''.join(f'<li>{html.escape(q["name"])}</li>' for q in ld('docs/index.html')['@graph'][1]['mainEntity'])
page = f'''<!doctype html><html lang="ru"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Verbisto — финал E9</title><style>body{{font:16px/1.5 system-ui;max-width:1200px;margin:0 auto;padding:24px;color:#1c1c1c}}
.g4{{display:grid;grid-template-columns:2fr 2fr 1fr 1fr;gap:12px;align-items:start}}.g2{{display:grid;grid-template-columns:1fr 1fr;gap:12px}}
figure{{margin:0}}figcaption{{font-size:13px;color:#666}}code{{background:#eef;padding:1px 4px;border-radius:4px}}td{{padding:4px 10px;border-bottom:1px solid #eee;vertical-align:top}}</style>
<h1>Verbisto — финальные страницы (принятый вид E9)</h1>
<p>Вёрстка — та, что вы приняли: в 48 местах из 48 (RU и EN; 1440 и 375 px; день и ночь; по 6 мест страницы) кадры финала совпали с E9 пиксель в пиксель (0,00 % отличий). Ниже — кадры самого финала.</p>
{rows}
<h2>Превью ссылки в соцсетях и мессенджерах (1200×630)</h2><div class=g2><figure>{img("docs/img/og-ru.jpg")}<figcaption>RU</figcaption></figure><figure>{img("docs/img/og-en.jpg")}<figcaption>EN</figcaption></figure></div>
<h2>Что добавлено</h2><table>
<tr><td>Значки App Store</td><td>3 на страницу, ведут на приложение id6836263523 с меткой места: <code>site-ru-hero</code>, <code>site-ru-plans</code>, <code>site-ru-end</code> (EN — так же с <code>en</code>)</td></tr>
<tr><td>Поиск</td><td>заголовок и описание RU/EN; связь RU ↔ EN для Google (для других языков — EN); основной адрес каждой страницы</td></tr>
<tr><td>Соцсети</td><td>превью выше: заголовок, описание, картинка</td></tr>
<tr><td>Карточка приложения для поиска</td><td>Verbisto · iOS 26 · образование · бесплатно скачать; вопросы-ответы — 10 настоящих вопросов страницы:<ol>{faq}</ol></td></tr>
<tr><td>Файлы сайта</td><td><code>sitemap.xml</code> (6 страниц), <code>robots.txt</code> (открыт всем, ИИ-поисковикам тоже), <code>llms.txt</code> (описание приложения для ИИ-помощников, по-английски)</td></tr>
</table>
<p><b>Не выложено.</b> Сайт в интернете пока старый: выкладка — только по вашему слову.</p></html>'''
open('design/pokaz-E9/final.html', 'w').write(page)
print(len(page.encode()) // 1024, 'КБ')
