# Сайт Verbisto на itoroapps.com/verbisto/ (репозиторий deneref/itoroapps-site, Pages: main /docs) из исходников design/:
#   design/dvizhenie-E9-en.html → /verbisto/        design/dvizhenie-E9.html → /verbisto/ru/
#   design/stranicy/privacy(-en).html, support(-en).html → /verbisto/[ru/]privacy/, /verbisto/[ru/]support/
# + ассеты (картинки → WebP, если легче), ссылки App Store, SEO (canonical, hreflang, OG/Twitter, JSON-LD), sitemap, llms.txt, ключ IndexNow.
# python3 -I design/instrumenty/sobrat.py   (из корня репо; ../itoroapps-site — клон deneref/itoroapps-site); перезаписывает docs/verbisto целиком.
import html as H, json, os, re, shutil
from PIL import Image
IG = None   # адрес аккаунта Instagram (https://www.instagram.com/<имя>/); пока None — значок из подвала вырезается, sameAs нет
SITE, B = 'https://itoroapps.com/verbisto/', '/verbisto/'
OUT = '../itoroapps-site/docs/verbisto'
STORE = 'https://apps.apple.com/app/apple-store/id6836263523?pt=129550662&amp;ct=site-{}-{}&amp;mt=8'
LINKS = {   # ссылка в исходнике → адрес на сайте (и в черновиках, и в правовых страницах)
    'dvizhenie-E9-en.html': B, 'dvizhenie-E9.html': B + 'ru/', 'en.html': B, 'index.html': B + 'ru/',
    'stranicy/privacy-en.html': B + 'privacy/', 'stranicy/privacy.html': B + 'ru/privacy/',
    'stranicy/support-en.html': B + 'support/', 'stranicy/support.html': B + 'ru/support/',
    'privacy-en.html': B + 'privacy/', 'privacy.html': B + 'ru/privacy/', 'support-en.html': B + 'support/', 'support.html': B + 'ru/support/'}
HOME = {
  'en': dict(src='design/dvizhenie-E9-en.html', path='', locale='en_US', og='og-en.jpg',
             og_alt='Verbisto: the app shows where a Spanish verb form went wrong'),
  'ru': dict(src='design/dvizhenie-E9.html', path='ru/', locale='ru_RU', og='og-ru.jpg',
             og_alt='Verbisto: тренажёр показывает, где ошибка в форме испанского глагола'),
}
LEGAL = [('privacy-en.html', 'privacy/', 'en', 'ru/privacy/'), ('privacy.html', 'ru/privacy/', 'ru', 'privacy/'),
         ('support-en.html', 'support/', 'en', 'ru/support/'), ('support.html', 'ru/support/', 'ru', 'support/')]

shutil.rmtree(OUT, ignore_errors=True)
for d in ('img', 'fonts', 'badges'): os.makedirs(f'{OUT}/{d}')

def put(src, folder, webp_ok=True):
    # копия в OUT/<folder>; jpg/png → WebP, если легче (скриншоты 3x — главный вес страницы); og и значок — как есть
    name = os.path.basename(src)
    if webp_ok and name.endswith(('.jpg', '.png')) and folder == 'img':
        webp = name.rsplit('.', 1)[0] + '.webp'
        Image.open(src).save(f'{OUT}/img/{webp}', 'WEBP', quality=85, method=6)
        if os.path.getsize(f'{OUT}/img/{webp}') < os.path.getsize(src): return B + 'img/' + webp
        os.remove(f'{OUT}/img/{webp}')
    shutil.copy2(src, f'{OUT}/{folder}/{name}')
    return f'{B}{folder}/{name}'

def assets(h, base):
    # url(…) и src="…" на img/ fonts/ badges/ (от папки исходника) → /verbisto/<папка>/<имя> (папка img/in/ сплющивается)
    def move(m):
        ref = m[2]; rel = os.path.normpath(os.path.join(base, ref))
        folder = next((f for f in ('img', 'fonts', 'badges') if rel.startswith(f'design/{f}/')), None)
        return m[0].replace(ref, put(rel, folder)) if folder else m[0]
    h = re.sub(r"url\((['\"]?)([^)'\"#]+)\1\)", move, h)
    return re.sub(r'(src)="([^"]+)"', lambda m: m[0] if re.match(r'data:|https?:', m[2]) else move(m), h)

def links(h):
    return re.sub(r'href="([^"#]+)"', lambda m: f'href="{LINKS.get(m[1], m[1])}"', h)

def strip_comments(h):
    h = re.sub(r'<!--.*?-->\n?', '', h, flags=re.S)
    h = re.sub(r'<style>.*?</style>', lambda m: re.sub(r'\s*/\*.*?\*/', '', m[0], flags=re.S), h, flags=re.S)
    def js(m):
        s = re.sub(r'^[ \t]*//.*\n', '', m[0], flags=re.M)          # строка-комментарий целиком
        return re.sub(r'(?<=[;{},)])[ \t]+//[^\n]*', '', s)          # хвостовой комментарий после кода
    return re.sub(r'<script>.*?</script>', js, h, flags=re.S)

def text(frag):
    return re.sub(r'\s+', ' ', H.unescape(re.sub(r'<[^>]+>', '', frag))).strip()

def faq(h):
    return [{'@type': 'Question', 'name': text(q), 'acceptedAnswer': {'@type': 'Answer', 'text': text(a)}}
            for q, a in re.findall(r'<details>\s*<summary>(.*?)</summary>(.*?)</details>', h, flags=re.S)]

def alternates(en, ru):
    return (f'<link rel="alternate" hreflang="en" href="{SITE}{en}">\n<link rel="alternate" hreflang="ru" href="{SITE}{ru}">\n'
            f'<link rel="alternate" hreflang="x-default" href="{SITE}{en}">\n')

def write(path, h):
    os.makedirs(os.path.dirname(f'{OUT}/{path}index.html'), exist_ok=True)
    open(f'{OUT}/{path}index.html', 'w', encoding='utf-8').write(h)
    left = re.findall(r'(?:url\(|src="|href=")(?!data:|https?:|#|\'\+|mailto:|\[)([^)"]+)', h)
    miss = [r for r in left if r.startswith(B) and not os.path.exists(OUT + '/' + r[len(B):])]
    other = [r for r in left if not r.startswith(B) and r != '/legal/']
    print(f'/verbisto/{path}', len(h.encode()), 'Б; нет файла:', miss or 0, '; чужие пути:', other or 0)
    return h

ICON = put('design/img/ikonka-120.png', 'img', False)
icon = Image.open('design/img/ikonka-120.png').resize((96, 96), Image.LANCZOS); icon.save(f'{OUT}/img/icon-96.png')
ICONS = f'<link rel="icon" type="image/png" sizes="96x96" href="{B}img/icon-96.png">\n<link rel="apple-touch-icon" href="{ICON}">\n'
e = lambda s: H.escape(s, quote=True)

for lang, p in HOME.items():
    h = open(p['src'], encoding='utf-8').read()
    h = links(strip_comments(assets(h, 'design')))
    h = re.sub(r'https://apps\.apple\.com/app/apple-store/id\[APP_ID\]\?pt=\[PROVIDER_ID\]&amp;ct=site-(\w+)-(\w+)&amp;mt=8',
               lambda m: STORE.format(m[1], m[2]), h)
    h = h.replace('[INSTAGRAM_URL]', IG) if IG else re.sub(r'<a class="ig".*?</a>', '', h, flags=re.S)
    url, og = SITE + p['path'], put('design/img/og/' + p['og'], 'img', False)
    title = text(re.search(r'<title>(.*?)</title>', h)[1])
    desc = H.unescape(re.search(r'<meta name="description" content="([^"]*)"', h)[1])
    ld = {'@context': 'https://schema.org', '@graph': [
        {'@type': 'MobileApplication', 'name': 'Verbisto', 'operatingSystem': 'iOS 26', 'applicationCategory': 'EducationalApplication',
         'inLanguage': ['en', 'ru'], 'description': desc, 'url': url,
         'sameAs': 'https://apps.apple.com/app/id6836263523',
         'offers': {'@type': 'Offer', 'price': '0', 'priceCurrency': 'USD'}},
        {'@type': 'FAQPage', 'inLanguage': lang, 'mainEntity': faq(h)}]}
    if IG: ld['@graph'].append({'@type': 'Organization', 'name': 'Verbisto', 'url': SITE, 'sameAs': [IG]})
    head = f'''<link rel="canonical" href="{url}">
{alternates('', 'ru/')}{ICONS}<link rel="preload" href="{B}fonts/Manrope.woff2" as="font" type="font/woff2" crossorigin>
<link rel="describedby" type="text/markdown" href="{B}llms.txt">
<meta name="apple-itunes-app" content="app-id=6836263523">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Verbisto">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:locale" content="{p['locale']}">
<meta property="og:locale:alternate" content="{HOME['en' if lang == 'ru' else 'ru']['locale']}">
<meta property="og:image" content="https://itoroapps.com{og}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{e(p['og_alt'])}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="https://itoroapps.com{og}">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
'''
    h = re.sub(r'(<meta name="description"[^>]*>\n)', lambda m: m[1] + head, h, count=1)
    write(p['path'], h)
    print('   вопросов FAQ:', len(ld['@graph'][1]['mainEntity']))

for src, path, lang, other in LEGAL:
    h = open('design/stranicy/' + src, encoding='utf-8').read()
    h = links(assets(h, 'design/stranicy'))
    en, ru = (path, other) if lang == 'en' else (other, path)
    h = h.replace('</head>', f'<link rel="canonical" href="{SITE}{path}">\n{alternates(en, ru)}{ICONS}</head>', 1)
    write(path, h)

urls = [('', 'ru/'), ('privacy/', 'ru/privacy/'), ('support/', 'ru/support/')]
alt = lambda en, ru: ''.join(f'\n    <xhtml:link rel="alternate" hreflang="{l}" href="{SITE}{u}"/>' for l, u in (('en', en), ('ru', ru), ('x-default', en)))
sm = ''.join(f'\n  <url>\n    <loc>{SITE}{u}</loc>{alt(en, ru)}\n  </url>' for en, ru in urls for u in (en, ru))
open(f'{OUT}/sitemap.xml', 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
                                      f'xmlns:xhtml="http://www.w3.org/1999/xhtml">{sm}\n</urlset>\n')
for f in os.listdir('design/stranicy'):
    if f.endswith('.txt'): shutil.copy2('design/stranicy/' + f, f'{OUT}/{f}')   # llms.txt, ключ IndexNow
print('sitemap:', sm.count('<loc>'), 'адресов; файлы:', sorted(os.listdir(OUT)))
