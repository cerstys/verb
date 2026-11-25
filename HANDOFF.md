# HANDOFF — сайт Verbisto и léxito (25.11.2026, СТОП по слову владельца)

Координатор — local_f6b2232e-ca44-4d05-a946-56e6db9c95c3. Владелец пишет и сам (часто через Remote Control с телефона).

## Где что живёт
- Сайт: `deneref/itoroapps-site` (клон `~/itoroapps-site`), Pages `main`/`docs`. `/verbisto/` EN, `/verbisto/ru/` RU, privacy/support.
- Источник: этот репозиторий (`cerstys/verb`, ветка `anim-i-proba`, выкладывается `git push origin anim-i-proba:main`).
  Вид: `design/dvizhenie-E9-en.html`, `design/dvizhenie-E9.html`; сборка `python3 -I design/instrumenty/sobrat.py` → `../itoroapps-site/docs/verbisto` (руками не править).
- Главную itoroapps.com собирает другая линия («Даня»), коммиты 23ff143, d47d137 — не трогать без слова владельца.

## Состояние сайта (itoroapps-site main 44737ca, verb main — последний коммит этой сессии)
- 24.11: EN без русского, полоса Safari, тёмный экран ввода, сцена с телефоном (см. git log).
- Поисковики и ИИ выложены (d738783): sitemap общий + verbisto, robots, ключ IndexNow, JSON-LD главной (Organization `#org`, ItemList léxito/Verbisto) и léxito (MobileApplication, FAQPage по 4 видимым вопросам), canonical и превью 1200×630 главной и léxito, `docs/llms.txt` в корне, плашка App Store в Safari на léxito.
- Сцена с телефоном (мобильный): фраза загорается, когда середина текста проходит **90%** высоты экрана, проявление .25s (3b688d3 / verb). **Владелец на телефоне не подтвердил** — спросить.
- `verbisto/llms.txt`: цены US $6.99/мес, $29.99/год, $79.99 навсегда с пометкой «по странам иначе» (44737ca). На страницах цен НЕТ — слово владельца (регионы разные), так же у léxito.

## Поисковики — сделано 25.11
- Google Search Console (Chrome владельца, аккаунт cerstys@, рядом oneofyours.ru): ресурс `https://itoroapps.com/` подтверждён файлом `docs/googleb2ba5f3e59b15710.html` (998ff0f, НЕ удалять). `sitemap.xml` — успешно, 6 стр.; `verbisto/sitemap.xml` при отправке «Не получено», но /verbisto/ уже найден по ней — **перепроверить**. Запрошена индексация /, /lexito/, /verbisto/.
- Bing Webmaster: подтверждён файлом `docs/BingSiteAuth.xml` (5c64b8a, НЕ удалять); обе карты отправлены (Processing). Разрешение bing.com на чтение GSC выдано; связки-импорта нет (мешала ручная запись) — не нужна.
- IndexNow: владелец отправил, 202. Повторять при новых страницах.
- В GSC появились ресурсы Instagram/TikTok/YouTube — предложено владельцу, не делано.

## Разбор смыслов (главная работа 25.11) — НЕ потерять
**Документ:** `design/razbor-smyslov-2026-11-25.md` (копия в заметках группы `ЛН-2-ЦА-смыслы-для-плана.md`). Там: сегменты ЦА с размерами и источниками, боли их словами, запросы к ИИ (EN/RU), конкуренты, предложения по страницам, карта «боль → ответ продукта» (от координатора, по коду), очерёдность времён.
**Ключевые находки:**
- ЦА шире: Verbisto — UK GCSE/A-level (136 871 в 2025), DELE A2 для гражданства Испании (~22,5 тыс. записей за 2 сессии 2025), переехавшие в Испанию, русско-/украиноязычные в Испании (объяснений на русском нет ни у кого), застрявшие в Duolingo. léxito — читатели B2+, живущие в Испании, «это слово грубое?» (сильный крючок), зрители сериалов из Испании, B2→C1.
- Свободная позиция: «Испания по умолчанию» (у конкурентов vosotros — переключатель); ни один список словарей не говорит об Испании vs Латинской Америке. Ближайший конкурент Verbisto — Ella Verbs ($59.99/год).
- Страницы открываются механикой, а не болью; H1 Verbisto «Where's the mistake?» без поисковых слов; «для кого» внизу; анимированные слова (`comereis`, `comeréis`) машина читает по буквам (aria-label на `<p>` не работает) — чинить скрытым целым словом + буквы `aria-hidden`.
**Ответы координатора (по коду master 4a2f4540):** разбор — 5 зон (ударение, основа, окончание, вспомогательный, причастие), отметка на буквах ответа, ответ не показывает до конца попыток, называет причину, две ошибки — обе, не уверен — честный отказ. Ошибка только в знаке — отдельный вердикт, не «неверно». Звука нет. Напоминание одно в день по желанию, тихое. Русский — везде, самостоятельные тексты. Формула: *Shows exactly where the mistake is — the stem, the ending, the accent or the helper verb — and explains the rule for that one spot. It doesn't type the answer for you.*
**Решения владельца 25.11:** число глаголов и список времён на сайт НЕ писать (растут) — «прошедшие и будущее сейчас, набор растёт»; режим сравнения — первой парой indefinido↔imperfecto, на сайт только после выхода; цены на страницах не ставить.
**Передано координатору для плана:** ЦА и боли; очерёдность времён presente → condicional → presente de subjuntivo → imperativo с vosotros (imperativo в roadmap нет — новая позиция); координатор передаёт владельцу.

## План правок страниц (предложен, НЕ начат — ждёт «да» владельца)
Verbisto (EN, затем RU):
1. title: «Verbisto — Spanish verb conjugation practice for Spain (vosotros included) · iPhone».
2. Над «Where's the mistake?» — строка смысла: A «Spanish verbs as Spain conjugates them — and exactly where your form went wrong.» или B «Know the rules but still get the forms wrong? See exactly which part is off.»; формулу разбора — из ответа координатора.
3. «Is it for you?» поднять во второй экран и назвать людей (GCSE/A-level, DELE A2 для гражданства, переезд в Испанию, «Duolingo не учит vosotros»); «не для вас» — начинающие, LatAm, Android (без перечня времён).
4. FAQ новые (их словами, в разметку FAQPage): путаю indefinido/imperfecto (без обещания режима); GCSE/A-level; DELE A2; какие времена (без списка); Spain или LatAm; одно ударение — не «неверно»; без звука и навязчивых уведомлений; объяснения на русском.
5. Текст для машин в анимированных словах.
6. Не трогать: «No points. No telling-off.», «Written for English speakers», «Practise first. Pay later.».
Рамки: `Conjugador/landing/forbidden-claims.txt` (нет «only app», «works offline», «scientifically», «remember forever»).
léxito (после ответов владельца на `design/lexito-voprosy-2026-11-25.md`, 15 вопросов — владелец запросит сам): подзаголовок-крючок «Is it slang, rude, old-fashioned — or only said in Latin America?», title со словами «Spain Spanish–English dictionary, slang, register», блок «Who it's for / not for», FAQ (rude?, LatAm?, offline, iPhone/iOS 26.5, язык определений, Kindle — если работает), уровень «B2» вместо «B1–B2» (ждёт слова).
Главная: строка смысла под заголовком «Two iPhone apps for Spanish as it's spoken in Spain: one for the words you read, one for the verb forms you type.» + «для кого» у карточек.

## Не сделано / следующая сессия
1. ~~Исследование запросов~~ — **сделано 25.11** (разбор §11): Trends, подсказки Google, выдача App Store, Google AI Mode вместо Perplexity (Perplexity требует входа). План правок Verbisto — `design/plan-pravok-verbisto-2026-11-25.md`, передан координатору.
2. ~~План правок Verbisto~~ — **EN выложен 25.11** (itoroapps-site e37c0c8, verb ca5aaf2): title, строка с пятью местами ошибки, «для кого» вторым экраном, FAQ 15, llms.txt (≠ Verbito), без «works offline». Сверка — `design/sverka-verbisto-en-2026-11-25.md`. IndexNow 202, GSC — запрос индексации /verbisto/. **RU выложен 25.11** (itoroapps-site 556c517, verb ecd657a), сверка `design/sverka-verbisto-ru-2026-11-25.md`; IndexNow 200, GSC — запрос индексации /verbisto/ru/ (карты в GSC — «Успешно», 6 стр.). Чек-лист «новая функция → правки сайта»: `design/chek-list-novaya-funkciya-verbisto.md`.
3. **léxito — СЛЕДУЮЩАЯ РАБОТА (слово владельца 25.11: «с вербисто закончили, теперь та же работа с лексито»).**
   Ответы владельца на 15 вопросов: `design/lexito-otvety-2026-11-25.md` (копия из Downloads) — прочитать целиком. Главное:
   - Шэр из Apple Books **не работает** (FIX-124 не сделан) — на странице не обещать. App Store обещает обратное — это координатору, не на страницу.
   - Источники: «Safari and other apps that share text»; Kindle не называть. Скриншоты: из галереи или через «Поделиться», лимита слов нет.
   - Грубое = `malson.` / «vulgar / taboo» (1 039 значений), «derogatory», «careful: regional trap» (424). `vulg.` = «nonstandard (uneducated)» — НЕ грубое.
   - Пометы не у каждого значения (регистр — 12 %); нет пометы = источник не пометил. Английский перевод у всех значений, испанское определение — у большинства частых.
   - «Best from B2». Оценки не упоминать. Цен на странице нет; llms.txt — $39.99/год, $99.99 навсегда, «US, may vary by country». Только iPhone. 108 058 статей («more than 100,000» — правда).
   - Не для: A1–A2, латиноамериканский вариант, нужен курс, произношение, ИИ-собеседник. Сценарий с сериалом — можно (слово руками), субтитры из Netflix — нельзя.
   - Сравнение с конкурентами по именам — **развилка владельцу**, умолчание «без имён».
   Порядок как у Verbisto: разбор смыслов §6 + реальные запросы для léxito (Trends уже есть в §11: spanish slang 20→32, spanishdict вдвое вниз; добавить подсказки Google/App Store и Google AI Mode по запросам léxito из §3) → план правок EN координатору → слово → правки (`~/itoroapps-site/docs/lexito/` — проверить, чем собирается: руками или своим сборщиком) → кадры → сверка «боли · люди · ИИ» + факты по ответам → выкладка по слову → RU. Новые вопросы о продукте — списком координатору.
4. Перепроверить статусы карт в GSC/Bing и индексацию /lexito/, /verbisto/; сцену с телефоном — подтверждение владельца.
5. App Store Connect URL Verbisto — у координатора (metadata.json Conjugador 20129112, отправляет он).

## Мины
- **Симуляторы**: «iPhone 17» и «iPhone 17 Rubezh2» — тестовые, НЕ трогать, Safari на них не открывать (сорвал рубеж ЕН-1). Нужен iOS — сначала спросить координатора, свой симулятор «Verbisto-site», df ≥ 12 ГиБ, после — удалить и написать ему. Доступ к устройству владелец даёт только сидя за Mac.
- Мобильный вид — `node design/instrumenty/cdp.mjs shot <url> 402 874 out.jpg <scroll|.селектор> 1 1500` (DARK=1 — ночь); режим `js` с промисом виснет.
- Локальный сервер — потоковый: `python3 -c "import http.server as h,functools as f;h.ThreadingHTTPServer(('127.0.0.1',8766),f.partial(h.SimpleHTTPRequestHandler,directory='/Users/AI/itoroapps-site/docs')).serve_forever()"` (простой http.server зависает на оборванном соединении).
- `curl` наружу запрещён — проверка выкладки через `gh api repos/deneref/itoroapps-site/pages/builds/latest`.
- Push и Pages — только по слову владельца; itoroapps-site общий с léxito и главной — трогать свои файлы.
