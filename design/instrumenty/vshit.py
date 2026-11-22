# Живая страница одним файлом: url(…) и src="…" на локальные файлы → data:URI (base64); ссылка RU/EN → соседний файл показа.
# python3 -I design/instrumenty/vshit.py   (из корня репо) → design/pokaz-E9/E9-ru.html и E9-en.html
import base64, mimetypes, os, re
D = 'design'
MIME = {'.ttf': 'font/ttf', '.svg': 'image/svg+xml'}
def data(path):
    m = MIME.get(os.path.splitext(path)[1]) or mimetypes.guess_type(path)[0]
    return f'data:{m};base64,' + base64.b64encode(open(path, 'rb').read()).decode()
def local(ref):
    p = os.path.normpath(os.path.join(D, ref))
    return p if os.path.isfile(p) else None
def inline(html):
    html = re.sub(r"url\((['\"]?)([^)'\"]+)\1\)", lambda m: f'url({data(local(m[2]))})' if local(m[2]) else m[0], html)
    return re.sub(r'src="([^"]+)"', lambda m: f'src="{data(local(m[1]))}"' if local(m[1]) else m[0], html)
os.makedirs(f'{D}/pokaz-E9', exist_ok=True)
for src, out in (('dvizhenie-E9.html', 'E9-ru.html'), ('dvizhenie-E9-en.html', 'E9-en.html')):
    h = inline(open(f'{D}/{src}', encoding='utf-8').read())
    h = h.replace('href="dvizhenie-E9-en.html"', 'href="E9-en.html"').replace('href="dvizhenie-E9.html"', 'href="E9-ru.html"')
    open(f'{D}/pokaz-E9/{out}', 'w', encoding='utf-8').write(h)
    left = re.findall(r'(?:url\(|src=")(?!data:|https?:|\'\+)([^)"]+)', h)
    print(out, len(h.encode()), 'не вшито:', left or 0)
