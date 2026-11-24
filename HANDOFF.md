# HANDOFF — сайт Verbisto (24.11.2026: переезд + Instagram ВЫЛОЖЕНЫ координатором — itoroapps-site main 5b1b4d2, verb main 72f5db5; проверены им вживую)

Координатор — сессия local_f6b2232e-ca44-4d05-a946-56e6db9c95c3. С владельцем — через координатора.

## Где что живёт
- **Новый адрес** (слово владельца 24.11 «ссылку на сайт такого вида», как itoroapps.com/lexito/): репозиторий `deneref/itoroapps-site` (у `cerstys` есть push), Pages `main` / `/docs`, клон `~/itoroapps-site`, ветка **`verbisto`** (не отправлена).
  - `/verbisto/` — EN (главный: упор владельца на англоязычных), `/verbisto/ru/` — RU; `/verbisto/[ru/]privacy/`, `/verbisto/[ru/]support/`.
  - Verbisto добавлен в список приложений на главной itoroapps.com; в подвале ссылка на `/legal/` (aviso legal того же владельца).
- **Источник и сборка** — этот репозиторий (`cerstys/verb`, ветка `anim-i-proba`):
  - вид: `design/dvizhenie-E9-en.html`, `design/dvizhenie-E9.html`; правовые страницы: `design/stranicy/*.html`; `llms.txt` и ключ IndexNow — там же; og — `design/img/og/`.
  - сборка: `python3 -I design/instrumenty/sobrat.py` → пишет `../itoroapps-site/docs/verbisto` целиком (руками не править).
  - картинки → WebP (если легче), шрифт `design/fonts/Manrope.woff2` (подмножество, 32 КБ), favicon 96 px из иконки.
- **Старый адрес** verbisto.itoroapps.com (`docs/` здесь): 6 страниц-переадресаций (meta refresh + canonical + noindex) на новые адреса, `CNAME`, `robots.txt`. Не удалять: на них ссылаются метаданные App Store (`design/vitrina/metadata.json` в репозитории приложения).

## Проверено
- Ссылки всех 6 страниц разрешаются (0 битых); sitemap 6 адресов с hreflang en/ru/x-default.
- Сверка `zsh design/instrumenty/sverka-final.sh` (сайт с `127.0.0.1:8766` против E9, RM=1, значок IG скрыт в обоих): 48 из 48 мест = 0,00 %.
- Ранее: FAQ без прыжка (≤ 0,4 px), woff2 vs TTF ≤ 0,44 % (сглаживание).

## Дальше (лендинг ведёт эта линия — слово владельца 24.11; координатор на сайте больше не действует)
- Выложено: itoroapps-site main 5b1b4d2 + edc4bfc координатора (корневой robots.txt, Sitemap → /verbisto/sitemap.xml); verb main 72f5db5. Координатор вживую: 8 страниц 200, IG на обеих, /legal/ → политика Verbisto, 6 старых адресов переадресуют.
- 1. «Сейчас она не открывается» (владелец): у координатора 200 со слэшем/без, с www. Спросить владельца: какой адрес и устройство; искать DNS, кеш, HTTPS на www/http, iOS Safari.
- 2. IndexNow: тело готово в /private/tmp/claude-501/lg/indexnow.json (urlList только /verbisto/, ключ там же). Координатору запрос НЕ разрешили — сам не слать в обход; спросить владельца.
- 3. Google Search Console и Bing Webmaster — входом владельца: sitemap, запрос индексации, смена адреса со старого поддомена.
- 4. App Store Connect (Privacy, Support, Marketing URL) и `design/vitrina/metadata.json` в репозитории приложения — тоже этой линии.
- Удаление `design/shots/` (≈64 МБ вне git) — спрошено, ответа нет.
- Instagram: `IG` = https://www.instagram.com/lexito.verbisto.apps/ (Organization itoroapps, sameAs).

## Инструменты
- `node design/instrumenty/cdp.mjs shot|el|js|frames|fps|trace …`; `CSS=…`, `RM=1`, `DARK=1` (оба одним вызовом — исправлено).
- Локальный сервер: `python3 -m http.server 8766 --bind 127.0.0.1 --directory ~/itoroapps-site/docs`.

## Мины
- Push и Pages — только по слову владельца; коммиты — поимённым `git add`.
- Скептика не звать. Слово «проба» в RU не использовать. EN-тариф — Lifetime.
- `itoroapps-site` общий с léxito (другой проект): трогать только `docs/verbisto/`, строку на главной и README.
