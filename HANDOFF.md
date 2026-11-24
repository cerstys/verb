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

## Выложено позже 24.11
- Сцена с телефоном (мобильный): IO заменён на линию 84% высоты экрана по середине текста фразы (itoroapps-site 0a43aed, verb be889bd). На телефоне владельца не проверено — ждать его слова.

## Не сделано / ждёт
0. Живой сайт после 5e9578c проверен (Pages built 5e9578c, кадр /verbisto/ ночью — норм).
1. **Поисковики и ИИ** — ветка `seo-oba` клона itoroapps-site (на main): 538e939 (sitemap, robots, ключ IndexNow), 7b65296 + fe65fc4 — главная и léxito (разрешение владельца 24.11): canonical léxito, превью 1200×630 `docs/img/og.jpg`, `docs/lexito/img/og.jpg`; JSON-LD: Organization `#org` (email hello@itoroapps.com, sameAs только Instagram — TikTok/YT владелец велел не ставить), léxito и Verbisto как MobileApplication, FAQPage léxito ровно по 4 видимым вопросам; `docs/llms.txt` в корне по фактам владельца (цены léxito $39.99/год и $99.99 навсегда, US; iOS 26.5+; EN/ES; >100 000 статей, «построено на данных Wiktionary», не «все определения из Wiktionary»; без скидок и процентов). Логотипа студии нет — в разметке пропущен. Расхождение: FAQ léxito на странице «Best from about B1–B2», владелец — B2+; в llms.txt B2+, страницу не правил — спросить. Плюс плашка App Store в Safari на léxito. **Выложено по слову владельца 24.11: itoroapps-site main d738783.**
2. Google Search Console — **сделано 24.11** в Chrome владельца (аккаунт, где уже oneofyours.ru): ресурс `https://itoroapps.com/` подтверждён HTML-файлом `docs/googleb2ba5f3e59b15710.html` (itoroapps-site 998ff0f, НЕ удалять); `sitemap.xml` — успешно, 6 стр.; `verbisto/sitemap.xml` при отправке «Не получено», но по ней Google уже нашёл /verbisto/ — перепроверить статус; запрошена индексация /, /lexito/ (был неизвестен), /verbisto/ (обнаружен, не проиндексирован). Заметка: в Search Console появились ресурсы Instagram/TikTok/YouTube — можно добавить профили, если владелец захочет.
3. Bing Webmaster — **сделано 24.11**: вход владельца через Google (cerstys@); импорт из GSC споткнулся о ручную запись — подтверждено файлом `docs/BingSiteAuth.xml` (itoroapps-site 5c64b8a, НЕ удалять); отправлены `sitemap.xml` и `verbisto/sitemap.xml` (Processing). Разрешение bing.com на чтение Search Console выдано. Новые карты сайта в Bing добавлять вручную (связки с GSC нет); новые страницы — через IndexNow.
5. Проверить завтра: статус обеих карт в Google и Bing, индексацию /lexito/ и /verbisto/; сцену с телефоном на телефоне владельца (линия 90%, itoroapps-site 3b688d3).
4. IndexNow — отправлено владельцем 24.11, ответ 202 (принято). Повторять только при новых страницах; тело `/private/tmp/claude-501/lg/indexnow.json`.
5. App Store Connect URL и `design/vitrina/metadata.json` в репо приложения — по слову владельца.

## Мины
- **Симуляторы**: «iPhone 17» и «iPhone 17 Rubezh2» — тестовые, НЕ трогать, Safari на них не открывать (сорвал рубеж ЕН-1). Нужен iOS — сначала спросить координатора, свой симулятор «Verbisto-site», df ≥ 12 ГиБ, после — удалить и написать ему. Доступ к устройству владелец даёт только сидя за Mac.
- Мобильный вид — `node design/instrumenty/cdp.mjs shot <url> 402 874 out.jpg <scroll|.селектор> 1 1500` (DARK=1 — ночь); режим `js` с промисом виснет.
- Локальный сервер — потоковый: `python3 -c "import http.server as h,functools as f;h.ThreadingHTTPServer(('127.0.0.1',8766),f.partial(h.SimpleHTTPRequestHandler,directory='/Users/AI/itoroapps-site/docs')).serve_forever()"` (простой http.server зависает на оборванном соединении).
- `curl` наружу запрещён — проверка выкладки через `gh api repos/deneref/itoroapps-site/pages/builds/latest`.
- Push и Pages — только по слову владельца; itoroapps-site общий с léxito и главной — трогать свои файлы.
