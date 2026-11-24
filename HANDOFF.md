# HANDOFF — сайт Verbisto (24.11.2026, поздний вечер)

Координатор — local_f6b2232e-ca44-4d05-a946-56e6db9c95c3. Владелец пишет и сам (часто через Remote Control с телефона).

## Где что живёт
- Сайт: `deneref/itoroapps-site` (клон `~/itoroapps-site`), Pages `main`/`docs`. `/verbisto/` EN, `/verbisto/ru/` RU, privacy/support.
- Источник: этот репозиторий (`cerstys/verb`, ветка `anim-i-proba`, выкладывается `git push origin anim-i-proba:main`).
  Вид: `design/dvizhenie-E9-en.html`, `design/dvizhenie-E9.html`; сборка `python3 -I design/instrumenty/sobrat.py` → `../itoroapps-site/docs/verbisto` (руками не править).
- Главную itoroapps.com собирает другая линия («Даня»), коммиты 23ff143, d47d137 — не трогать без слова владельца.

## Выложено сегодня (itoroapps-site main, последнее 5e9578c; verb main 43978c2)
- EN без русского: раздел «Written for English speakers», FAQ, meta, RU-переключатель убран из EN-шапок (вкл. privacy/support).
- Белая полоса внизу в Safari 26+: `.glints` height calc(100lvh + 200px).
- Мобильная сцена с телефоном: `.cam` .7, шаги 20vh, IO rootMargin '-55% 0px -24% 0px' — фраза меняется посередине свободной зоны (по замечаниям владельца, кадры headless 402×874).
- Тёмная тема экрана ввода «You type it»: кадры `design/img/vvod-*-noch.*`, исходники 1206×2622 в `design/img/in-dark/`; @media dark в обоих HTML; рамка кнопки в ночи top 58.73% h 6.33%.
- Проверено: ссылки App Store id6836263523 = Verbisto, id6820599112 = léxito; Instagram один — lexito.verbisto.apps (имя профиля всё ещё «metículo · verbisto» — сказано владельцу, менять ему).

## Не сделано / ждёт
0. Живой сайт после 5e9578c проверен (Pages built 5e9578c, кадр /verbisto/ ночью — норм).
1. **Поисковики** — ветка `seo-oba` клона itoroapps-site перебазирована на main: 538e939 (sitemap, robots, ключ IndexNow, README) + 7b65296 (JSON-LD в главной: Organization `#org` + ItemList двух MobileApplication, цена 0, App Store в sameAs; без рейтингов — их нет, rich result приложений Google без aggregateRating/review не даёт, это ок). Визуально главная не меняется. **НЕ отправлено — ждёт слова владельца**: `cd ~/itoroapps-site && git checkout main && git merge --ff-only seo-oba && git push origin main`.
2. Google Search Console (после п.1): ресурс URL-prefix `https://itoroapps.com/`, способ «HTML-файл» — Google выдаёт файл `googleXXXX.html` только после входа; положить в `docs/` как есть (не переименовывать, без переадресаций), выложить, нажать «Подтвердить». Потом карты `sitemap.xml` и `verbisto/sitemap.xml`, запрос индексации `/`, `/lexito/`, `/verbisto/`. Вход — владельца во встроенном браузере на Mac.
3. Bing Webmaster — «Импорт из Google Search Console» (после п.2), вход владельца.
4. IndexNow (после п.1): тело `/private/tmp/claude-501/lg/indexnow.json`; команда владельца:
   `curl -s -o /dev/null -w '%{http_code}\n' -X POST https://api.indexnow.org/indexnow -H 'Content-Type: application/json; charset=utf-8' --data @/private/tmp/claude-501/lg/indexnow.json` (200/202 — ок).
5. App Store Connect URL и `design/vitrina/metadata.json` в репо приложения — по слову владельца.

## Мины
- **Симуляторы**: «iPhone 17» и «iPhone 17 Rubezh2» — тестовые, НЕ трогать, Safari на них не открывать (сорвал рубеж ЕН-1). Нужен iOS — сначала спросить координатора, свой симулятор «Verbisto-site», df ≥ 12 ГиБ, после — удалить и написать ему. Доступ к устройству владелец даёт только сидя за Mac.
- Мобильный вид — `node design/instrumenty/cdp.mjs shot <url> 402 874 out.jpg <scroll|.селектор> 1 1500` (DARK=1 — ночь); режим `js` с промисом виснет.
- Локальный сервер — потоковый: `python3 -c "import http.server as h,functools as f;h.ThreadingHTTPServer(('127.0.0.1',8766),f.partial(h.SimpleHTTPRequestHandler,directory='/Users/AI/itoroapps-site/docs')).serve_forever()"` (простой http.server зависает на оборванном соединении).
- `curl` наружу запрещён — проверка выкладки через `gh api repos/deneref/itoroapps-site/pages/builds/latest`.
- Push и Pages — только по слову владельца; itoroapps-site общий с léxito и главной — трогать свои файлы.
