# HANDOFF — сайт Verbisto (заход ЛН-1 закрыт 17.11.2026, сессия в архиве)

Итог зафиксирован по слову владельца 17.11: «по лендингу точно нужно зафиксировать все что мы получили локально».
Координатор — ветка `claude/parallel-work-organization-50228d` в `/Users/AI/Conjugador`.

## Что опубликовано
- Адрес: **https://verbisto.itoroapps.com/** — HTTPS выпущен GitHub, «Enforce HTTPS» включён владельцем 17.11.
- Страницы (RU / EN): `index.html` / `en.html` — лендинг; `privacy.html` / `privacy-en.html` — политика;
  `support.html` / `support-en.html` — поддержка. Подвал каждой ведёт на политику и поддержку своего языка, hreflang RU↔EN.
- Для App Store Connect: Privacy Policy URL — https://verbisto.itoroapps.com/privacy.html (EN — privacy-en.html);
  Support URL — https://verbisto.itoroapps.com/support.html (EN — support-en.html).

## Как устроено
- Репозиторий **`cerstys/verb`** на GitHub, публичный (бесплатный Pages работает только у публичного). Ветка `main`.
- GitHub Pages: источник — `main` / папка **`/docs`**. Настройки: https://github.com/cerstys/verb/settings/pages
- Свой адрес: файл `docs/CNAME` = `verbisto.itoroapps.com` (коммит 32ebf75).
- DNS домена `itoroapps.com` — у Squarespace (NS `nsd1/nsd2.squarespacedns.com`): запись **CNAME `verbisto` → `cerstys.github.io.`**
  (проверено `dig` 17.11). Почта домена — Google (MX `smtp.google.com`), ящик поддержки `verbisto@itoroapps.com`.
- Если HTTPS слетит: в настройках Pages стереть Custom domain → Save → вписать снова → Save; GitHub перевыпустит сертификат.
- Push с этого Mac идёт по сохранённому токену владельца (Связка ключей).
- Без JS, аналитики, куки и CDN; шрифт Manrope локально (`docs/fonts/`), значки App Store — `docs/badges/`, кадры — `docs/img/`.

## Содержание и источники
- Название **Verbisto** (решение владельца 17.11 «берем verbisto»; разбор — `design/nazvanie/` в ветке координатора Conjugador).
- Тексты лендинга — методист (заказы 135, 141; C-288, C-294); первый экран — вариант 1 маркетолога-3 («берём»).
- Политика — дословно `PrivacyPolicy.json` приложения (master) с данными владельца: Daniel Mokeev Toro, Мадрид, Испания,
  verbisto@itoroapps.com; вступает в силу 17 ноября 2026 г. При правке политики в приложении — перенести сюда тем же днём.
- Факты на странице: проба 7 дней только у годовой подписки, напоминание за 2 дня; Семейный доступ — только «Навсегда»;
  прогресс на устройстве, отмена оплаты его не стирает. Subjuntivo и condicional не упоминать.
- Черновики и разборы (маркетологи, копирайтер, эксперт, варианты первого экрана) — в `design/`, на сайт не публикуются.

## Не сделано
- Кнопки App Store — заготовки: нет Apple ID приложения и Provider ID (`pt=`) до появления приложения в App Store Connect;
  метки кампаний `ct=site-ru-hero` / `site-ru-end` / `-en-` уже стоят.
- КП-1 (координатор): п. 2 — политика о небуквенных знаках, п. 3 — тексты страницы поддержки — ждут методиста.

## Мины
- Push и правки Pages — только по слову владельца. `curl` координатору запрещён; сайт проверять встроенным браузером.
- Рамка кадров: `/Volumes/Bezel-iPhone-17` «iPhone 17 – Black – Portrait», окно 1206×2622 @72,69; углы экрана срезать по корпусу.
- Источник кадров приложения — эталоны в `/Users/AI/Conjugador/design/ekrany/`.
