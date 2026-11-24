# HANDOFF — сайт Verbisto (24.11.2026: переезд + Instagram собраны и проверены, НЕ выложены — ждут подтверждения владельца в окне сессии)

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

## Ждёт владельца
- **Готово к публикации:** itoroapps-site `verbisto` = 5b1b4d2 (поверх 8a19516, f11470e координатора) → слить в `main`, push; verb `anim-i-proba` = bc33c1e+ → слить в `main`, push. Сначала itoroapps-site. Слово владельца передано координатором («да, выкладывай…»), подтверждение в окне этой сессии не получено — push не делался (СТОП по шву 300 тыс.).
- После push: вживую /verbisto/, /verbisto/ru/, обе политики, обе поддержки, /legal/, переадресации verbisto.itoroapps.com/privacy-en.html и support-en.html; записка координатору. App Store Connect и metadata.json делает координатор.
- Instagram вписан: `IG` = https://www.instagram.com/lexito.verbisto.apps/ (Organization itoroapps, sameAs); сверка 0,00 % со значком.
- Правовое сверено координатором 24.11: тексты 4 страниц = опубликованные (verb origin/main 32ebf75); /legal/ — абзац «Data protection» со ссылками на 3 политики (коммит координатора 8a19516 поверх 5f111f2 в ветке `verbisto`; ветку без него не переписывать).
- Слово на push: `~/itoroapps-site` ветка `verbisto` → `main` (это выкладка itoroapps.com) и `anim-i-proba` здесь (переадресации старого адреса). Выкладывать вместе.
- После выкладки: App Store Connect — Marketing URL `https://itoroapps.com/verbisto/`, Privacy `…/verbisto/privacy/`, Support `…/verbisto/support/`; поправить `metadata.json` в репозитории приложения (через координатора). Search Console и Bing — сразу на новый адрес; IndexNow — один POST после выкладки.
- Удаление `design/shots/` (≈64 МБ вне git) — спрошено, ответа нет.

## Инструменты
- `node design/instrumenty/cdp.mjs shot|el|js|frames|fps|trace …`; `CSS=…`, `RM=1`, `DARK=1` (оба одним вызовом — исправлено).
- Локальный сервер: `python3 -m http.server 8766 --bind 127.0.0.1 --directory ~/itoroapps-site/docs`.

## Мины
- Push и Pages — только по слову владельца; коммиты — поимённым `git add`.
- Скептика не звать. Слово «проба» в RU не использовать. EN-тариф — Lifetime.
- `itoroapps-site` общий с léxito (другой проект): трогать только `docs/verbisto/`, строку на главной и README.
