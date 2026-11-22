# HANDOFF — сайт Verbisto (22.11.2026: заход «анимация и проба», E9 — EN доведена, ждёт вида владельца)

Координатор — сессия local_f6b2232e-ca44-4d05-a946-56e6db9c95c3 (ветка `claude/parallel-work-organization-50228d` в `/Users/AI/Conjugador`). С владельцем — через координатора.

## Опубликовано (без изменений с ЛН-1, 17.11)
- https://verbisto.itoroapps.com/ — репозиторий `cerstys/verb`, Pages: `main` / `/docs`. Локальный `main` впереди `origin` на 1 коммит (e188d0f), не отправлен.

## Ветка `anim-i-proba` — текущий черновик E9
- RU: `design/dvizhenie-E9.html`; EN: `design/dvizhenie-E9-en.html` (структура RU, тексты — копирайтер, отчёт `design/teksty-en-E9.md`); старая EN — `design/dvizhenie-E9-en-staraya.html`.
- История кругов 1–8 — `design/otchet-2026-11-21-animacii.md`. Принято владельцем: концовка comeréis (не трогать), пятна синие, клавиши без подсветки, RU-тексты нравятся.
- «Год»: разведка `design/god-razvedka.md` → эскизы E8 `design/god-sayty-E8.html` → владелец выбрал B → `design/god-B2.html` → в E9 раздел «Как платить» (кадры `refs/god/e9-*.jpg`).

## Замечания владельца 22.11 — состояние
1. Волна-подчёркивание в герое — СДЕЛАНО (062bfb1): гребень по целому счётчику (был дробный остаток → разные верхушки), кривая в em. Кадры было/стало RU: `design/shots/e9-volna/vblizi-*.jpg`; EN (1440 и 375): `design/shots/e9-volna-en/vblizi-*-en.jpg` — гребни ровные (контрольные точки 5/15 чередуются).
2. Рамки телефона — официальная Apple iPhone 17 Mist Blue (`design/img/ramka-iphone17-mist-blue.png`; довод: холодный голубой обод в синей палитре). RU — 8ea122c; EN — в wip-коммите.
3. EN по структуре RU — текст готов (копирайтер, general-purpose; кириллица вне комментариев 0). EN-разбор — кадр `img/in/razbor-en-light|dark.png`. Экран ввода EN — настоящие кадры приложения (`img/vvod-en-k0|k2-3x.jpg`, `img/vvod-en-check-3x.png`; фишки и крестик общие с RU). Листы RU | EN: `design/shots/e9-ru-en/ryadom-{1440,375}-{den,noch}.jpg`.
4. Копирайтер ≠ методист (слово владельца): EN пишет general-purpose с ролью «копирайтер лендингов…».

## QA-заход 22.11 (2 замечания владельца + 3 QA-агента sonnet/high: RU 1440/1024, EN 1440/1024, телефоны 320–430)
- Показ владельцу «было/стало»: `design/pokaz-E9/qa-bylo-stalo.html` (картинки вшиты). Живые страницы: `design/pokaz-E9/E9-ru|en.html` — пересобирать `python3 -I design/instrumenty/vshit.py`.
- Исправлено: выносные `.tact h2` (padding-block .15em); фишки не спускаются на кнопки (окно 162 px @3x); маска поля внутри скруглений; мобильный фон липкого телефона — во всю ширину, мягкие края; ≤360 px телефон ×0,68 и строка разбора 26 px; смена примера 460 мс; сброс набора — сначала фишки; кнопка 0,1 с; text-wrap balance/pretty + nbsp; EN-кавычки.
- Не правлено (довод в показе): двойной ободок «Check» — родной вид приложения; тарифы по низу — намеренно; резерв высоты карточки героя; 150 % текста — эмуляция Chrome, не iOS.
- Кадры QA `design/shots/qa-E9/` — не в git (≈550 jpeg), удалить после принятия.

## Недоделано
- Вид — владельцу (показ выше); Safari/iPhone глазами не проверены. Затем очередь ниже.

## Очередь — ПОСЛЕ окончательного принятия вида владельцем
1. Ссылка значка App Store: `href="https://apps.apple.com/app/apple-store/id6836263523?pt=129550662&ct=site-<ru|en>-<hero|plans|end>&mt=8"` (Provider ID от владельца 21.11; `ct=site` не брать).
2. SEO RU+EN: title/description, canonical, hreflang ru/en/x-default, OG/Twitter, JSON-LD `SoftwareApplication` + `FAQPage`, `sitemap.xml`, `robots.txt` (AI-краулеры не закрывать), `llms.txt`, alt, заголовки; сверять браузером на опубликованном сайте.

## Инструменты
- Съёмка без сервера (сервер `http.server` авто-режим не пустил): `node design/instrumenty/cdp.mjs el|shot|js "file://…/dvizhenie-E9.html" …`; режим `js` выполняет сценарий и печатает его результат. 375 — масштаб 2; jpeg.

## Мины
- Push и Pages — только по слову владельца; в `docs/` — только после выбора; коммиты — поимённым `git add`.
- Скептика не звать (слово владельца). Слово «проба» в RU не использовать; в «Годе» нет «Отменить…» (только FAQ). EN-тариф — Lifetime.
- Диск почти полон: кадры jpeg, видео не копить.
