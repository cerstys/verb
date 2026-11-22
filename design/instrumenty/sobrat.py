# Боевые страницы из принятых черновиков: design/dvizhenie-E9(-en).html → docs/index.html, docs/en.html
# + ассеты в docs/img, ссылки App Store, SEO (canonical, hreflang, OG/Twitter, JSON-LD), sitemap/robots/llms.
# python3 -I design/instrumenty/sobrat.py   (из корня репо); повторный запуск переписывает всё заново.
import html as H, json, os, re, shutil
SITE = 'https://verbisto.itoroapps.com/'
STORE = 'https://apps.apple.com/app/apple-store/id6836263523?pt=129550662&amp;ct=site-{}-{}&amp;mt=8'
PAGES = {
  'ru': dict(src='design/dvizhenie-E9.html', out='docs/index.html', url=SITE, locale='ru_RU',
             links={'../docs/en.html': 'en.html'}, og='img/og-ru.jpg',
             og_alt='Verbisto: тренажёр показывает, где ошибка в форме испанского глагола'),
  'en': dict(src='design/dvizhenie-E9-en.html', out='docs/en.html', url=SITE + 'en.html', locale='en_US',
             links={'dvizhenie-E9.html': 'index.html', '../docs/privacy-en.html': 'privacy-en.html',
                    '../docs/support-en.html': 'support-en.html'}, og='img/og-en.jpg',
             og_alt='Verbisto: the app shows where a Spanish verb form went wrong'),
}
os.makedirs('docs/img', exist_ok=True)

def assets(h):
    # url(img/…) → docs/img/<имя> (папка in/ сплющивается), ../docs/… → корень сайта
    def move(m):
        ref = m[2]
        if ref.startswith('../docs/'): return m[0].replace(ref, ref[8:])
        if not ref.startswith('img/'): return m[0]
        name = os.path.basename(ref)
        shutil.copy2('design/' + ref, 'docs/img/' + name)
        return m[0].replace(ref, 'img/' + name)
    h = re.sub(r"url\((['\"]?)([^)'\"#]+)\1\)", move, h)
    return re.sub(r'(src)="([^"]+)"', lambda m: move(m) if m[2].startswith(('img/', '../docs/')) else m[0], h)

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

for lang, p in PAGES.items():
    h = open(p['src'], encoding='utf-8').read()
    h = strip_comments(assets(h))
    h = re.sub(r'https://apps\.apple\.com/app/apple-store/id\[APP_ID\]\?pt=\[PROVIDER_ID\]&amp;ct=site-(\w+)-(\w+)&amp;mt=8',
               lambda m: STORE.format(m[1], m[2]), h)
    for a, b in p['links'].items(): h = h.replace(f'href="{a}"', f'href="{b}"')
    title = text(re.search(r'<title>(.*?)</title>', h)[1])
    desc = H.unescape(re.search(r'<meta name="description" content="([^"]*)"', h)[1])
    ld = {'@context': 'https://schema.org', '@graph': [
        {'@type': 'MobileApplication', 'name': 'Verbisto', 'operatingSystem': 'iOS 26', 'applicationCategory': 'EducationalApplication',
         'inLanguage': ['ru', 'en'], 'description': desc, 'url': p['url'],
         'sameAs': 'https://apps.apple.com/app/id6836263523',
         'offers': {'@type': 'Offer', 'price': '0', 'priceCurrency': 'USD'}},
        {'@type': 'FAQPage', 'inLanguage': lang, 'mainEntity': faq(h)}]}
    e = lambda s: H.escape(s, quote=True)
    head = f'''<link rel="canonical" href="{p['url']}">
<link rel="alternate" hreflang="ru" href="{SITE}">
<link rel="alternate" hreflang="en" href="{SITE}en.html">
<link rel="alternate" hreflang="x-default" href="{SITE}en.html">
<link rel="describedby" type="text/markdown" href="/llms.txt">
<meta name="apple-itunes-app" content="app-id=6836263523">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Verbisto">
<meta property="og:url" content="{p['url']}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:locale" content="{p['locale']}">
<meta property="og:locale:alternate" content="{PAGES['en' if lang == 'ru' else 'ru']['locale']}">
<meta property="og:image" content="{SITE}{p['og']}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{e(p['og_alt'])}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{SITE}{p['og']}">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
'''
    h = re.sub(r'(<meta name="description"[^>]*>\n)', lambda m: m[1] + head, h, count=1)
    open(p['out'], 'w', encoding='utf-8').write(h)
    left = re.findall(r'(?:url\(|src="|href=")(?!data:|https?:|#|\'\+|mailto:)([^)"]+)', h)
    miss = [r for r in left if not os.path.isfile('docs/' + r.lstrip('/'))]
    print(p['out'], len(h.encode()), 'Б; вопросов FAQ:', len(ld['@graph'][1]['mainEntity']), '; нет файла:', miss or 0,
          '; design/ localhost:', len(re.findall(r'design/|localhost', h)))
