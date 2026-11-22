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

## Недоделано (следующий ход)
- Вид RU и EN — владельцу (листы выше), затем очередь ниже.
- Находка, не правлено: в RU `img/vvod-k0-3x.jpg` курсор зашит в кадр, поверх — живой `.vcar` → мигание не видно. EN-кадр без курсора.
- Рецепт EN-кадров приложения: временный XCUITest (класс в конце `DrillShotsUITests.swift`, не в git) на сборке 8b5093fa, `-appLocale en`, «I don't know → позже» до HABLAR·vosotros, набор hablareis, фишка 3; пузырь AutoFill на «пусто» заплатан фоном RU-кадра.

## Очередь — ПОСЛЕ окончательного принятия вида владельцем
1. Ссылка значка App Store: `href="https://apps.apple.com/app/apple-store/id6836263523?pt=129550662&ct=site-<ru|en>-<hero|plans|end>&mt=8"` (Provider ID от владельца 21.11; `ct=site` не брать).
2. SEO RU+EN: title/description, canonical, hreflang ru/en/x-default, OG/Twitter, JSON-LD `SoftwareApplication` + `FAQPage`, `sitemap.xml`, `robots.txt` (AI-краулеры не закрывать), `llms.txt`, alt, заголовки; сверять браузером на опубликованном сайте.

## Инструменты
- Съёмка без сервера (сервер `http.server` авто-режим не пустил): `node design/instrumenty/cdp.mjs el|shot|js "file://…/dvizhenie-E9.html" …`; режим `js` выполняет сценарий и печатает его результат. 375 — масштаб 2; jpeg.

## Мины
- Push и Pages — только по слову владельца; в `docs/` — только после выбора; коммиты — поимённым `git add`.
- Скептика не звать (слово владельца). Слово «проба» в RU не использовать; в «Годе» нет «Отменить…» (только FAQ). EN-тариф — Lifetime.
- Диск почти полон: кадры jpeg, видео не копить.
