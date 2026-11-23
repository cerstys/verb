# HANDOFF — сайт Verbisto (23.11.2026: финал E9 + скорость + Instagram в черновиках; НЕ выложен)

Координатор — сессия local_f6b2232e-ca44-4d05-a946-56e6db9c95c3 (ветка `claude/parallel-work-organization-50228d` в `/Users/AI/Conjugador`). С владельцем — через координатора.

## Опубликовано (без изменений с ЛН-1, 17.11)
- https://verbisto.itoroapps.com/ — репозиторий `cerstys/verb`, Pages: `main` / `/docs`. Локальный `main` впереди `origin` на 1 коммит (e188d0f), не отправлен.

## Ветка `anim-i-proba`
- Черновики (источник): RU `design/dvizhenie-E9.html`, EN `design/dvizhenie-E9-en.html`. Принято владельцем 22.11: «хорошо всё поправлено… пускай соберёт финальные версии».
- История: круги 1–8 — `design/otchet-2026-11-21-animacii.md`; «Год» → `design/god-B2.html`; EN-тексты — `design/teksty-en-E9.md`; QA — `design/pokaz-E9/qa-bylo-stalo.html`.

## Финал (22.11) — `docs/index.html`, `docs/en.html`
- Сборка: `python3 -I design/instrumenty/sobrat.py` (из корня) — черновик → `docs/`, картинки в `docs/img/` (папка `in/` сплющена), комментарии HTML/CSS/JS сняты, ссылки App Store `id6836263523?pt=129550662&ct=site-<ru|en>-<hero|plans|end>&mt=8`, SEO в `<head>`. Правка вида — в черновике, затем пересборка.
- SEO: canonical; hreflang ru/en + x-default → EN (для прочих языков EN понятнее); `rel=describedby` → `/llms.txt`; `apple-itunes-app`; OG/Twitter (`img/og-ru|en.jpg`, 1200×630, снято с героя zoom .74); JSON-LD `MobileApplication` (price 0, EducationalApplication, iOS 26) + `FAQPage` (10 вопросов — из `<details>` страницы).
- Файлы: `docs/sitemap.xml` (6 адресов с hreflang), `docs/robots.txt` (всё открыто), `docs/llms.txt` (EN, формат v2).
- Нет рейтинга → Google не даст звёздную карточку (нужен aggregateRating/review); выдумывать нельзя — добавить, когда появятся оценки в App Store.
- Сверка: `zsh design/instrumenty/sverka-final.sh` — E9 vs финал, RU/EN × 1440/375 × день/ночь × 6 мест, RM=1: 48 из 48 = 0,00 % (3 ночных 375 сначала 2–3 % — момент съёмки липкого телефона; при ожидании 2,5 с — 0,00 %). Кадры `design/shots/final-E9/` (не в git).
- Показ владельцу: `design/pokaz-E9/final.html` (самодостаточный; `python3 -I design/instrumenty/pokaz-final.py`).
- Проверено: шрифт грузится, 3 картинки + фоны грузятся, JS после снятия комментариев проходит `node --check`, анимация героя в финале = E9.

## 23.11 — сделано
- FAQ: прыжок 8 px при закрытии убран (7614859).
- Скорость (слово владельца «картинки и первый экран делаем»): сборщик кладёт WebP (q85), если он легче; шрифт — `docs/fonts/Manrope.woff2` (подмножество: латиница+Latin-1, кириллица, знаки; 165 КБ → 32 КБ; `Manrope.ttf` оставлен для старых черновиков) + preload в `<head>`; privacy/support тоже на woff2. Вес картинок+шрифта без og: RU 1 326 → 348 КБ, EN 1 462 → 350 КБ. Первый экран — текст и блики из canvas, фото на нём нет.
- Сверка 48/48 = 0,00 % (WebP vs исходники); woff2 vs TTF 20 мест: 375 — 0,00 %, 1440 — ≤ 0,44 % (сглаживание, буквы те же).
- Instagram: официальный SVG Meta в `design/img/ig/` (+README с правилами), в подвале обоих черновиков значок 29 px + подпись («Мы в Instagram» / «Follow us on Instagram») — выбор владельца. Ссылка — `[INSTAGRAM_URL]`; в `sobrat.py` `IG = None` → значок вырезается из финала, sameAs (Organization) не пишется. Получим адрес — вписать в `IG`, пересобрать.
- IndexNow: ключ `docs/93833476d0c3446e3902c664fc65b705.txt`; после выкладки — один POST на api.indexnow.org со списком адресов.
- cdp.mjs: RM и DARK в одном setEmulatedMedia (раньше DARK затирал RM — ночные кадры шли без reduced motion); профиль удаляется с повтором.
- Владелец: Яндекс — не нужен (упор на англоязычных). Его дела: слово на выкладку, Search Console (DNS TXT), Bing Webmaster (импорт из GSC), Marketing URL в App Store Connect, ссылка на сайт в профиле Instagram, адрес аккаунта нам.

## Недоделано
- Push и выкладка — ждут слова владельца. После выкладки: сверить в браузере на живом сайте (Rich Results Test, превью ссылки).
- Safari/iPhone глазами не проверены (WebP/woff2 Safari поддерживает).
- Нет адреса Instagram.
- `design/shots/qa-E9/` (≈550 jpeg, не в git) — удалить (у меня удаление не разрешено).

## Инструменты
- Съёмка без сервера: `node design/instrumenty/cdp.mjs el|shot|js "file://…" …`; `CSS=…` — вставить стиль, `RM=1`, `DARK=1`. 375 — масштаб 2; jpeg.

## Мины
- Push и Pages — только по слову владельца; коммиты — поимённым `git add`.
- Скептика не звать (слово владельца). Слово «проба» в RU не использовать; в «Годе» нет «Отменить…» (только FAQ). EN-тариф — Lifetime.
- Диск почти полон: кадры jpeg, видео не копить.
