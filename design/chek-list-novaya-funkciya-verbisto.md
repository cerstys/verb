# Чек-лист «новое время или функция Verbisto → правки сайта и витрины»

25.11.2026. Правило владельца: число глаголов и перечень времён на сайт не пишем (растут) — «прошедшие и будущее сейчас,
набор растёт». Новое на сайт — только после выхода в App Store. Цены — только в llms.txt.

## 1. Факты в коде (сначала сверить здесь)
| Что | Где | Что смотреть |
|---|---|---|
| Места ошибки | `~/Conjugador/Conjugador/Engines/MissLocation.swift:44` (`Zone`) | новая зона → перечень «stem, ending, accent, helper verb or participle» везде ниже |
| Бесплатные времена | `~/Conjugador/Conjugador/Engines/EngineConfig.swift:13` (`freeTenseIds`) | меняется → все «Indefinido and Perfecto are free forever» |
| Проба и напоминания | `EngineConfig.swift` (`trialReminderDaysBefore`, напоминания) | FAQ про пробу и «Will it nag me» |
| Рамки формулировок | `~/Conjugador/landing/forbidden-claims.txt` | новое обещание — не из списка; новая опасная фраза — дописать туда |

## 2. Страницы (исходники в `design/`, сборка `python3 -I design/instrumenty/sobrat.py`, руками docs не править)
| Место | Файл | Что меняется при новом времени | …при новой функции |
|---|---|---|---|
| title, description (→ og/twitter, JSON-LD `MobileApplication.description`) | `dvizhenie-E9-en.html` стр. 7–8, `dvizhenie-E9.html` стр. 7–8 | обычно ничего (времён в них нет) | если функция — главное отличие |
| Строка над H1 (пять мест) | там же, `.kicker` | — | новая зона ошибки |
| Первый экран: пример `comer · Futuro Simple` + JS-примеры `ex=[…]` | там же, `.sheet` и `<script>` | можно добавить пример нового времени (вид!) | — |
| Строка под кнопкой и в конце (`.pay`) | там же, 2 места | если новое время бесплатное | — |
| «Is it for you? / Подойдёт ли вам» | там же, `.fit` | **presente**: убрать из «не для» нечего (его там нет); можно добавить людей (GCSE Foundation, A1–A2) | если функция открывает новую группу |
| Блоки механики (You type it / breaks it down / hard ones come back) | там же | — | функция про разбор, повтор, ввод |
| FAQ (→ JSON-LD `FAQPage` собирается сам) | там же, `<details>` | «Which tenses / Какие времена» — формулировка без перечня; «GCSE», «DELE A2», «preterite vs imperfect» — ответы, где сказано «past tenses and the future» | **режим сравнения** — FAQ «mixing up preterite and imperfect / путаю indefinido и imperfecto» сейчас его не обещает; после выхода — сказать прямо |
| FAQ «Spain or Latin American» | там же | если время ведёт себя по-разному (imperativo с vosotros) | — |
| Support | `design/stranicy/support(-en).html` | проверить, нет ли перечня | новые вопросы поддержки |
| Главная itoroapps.com (линия «Даня») | `~/itoroapps-site/docs/index.html` | не трогать без слова владельца; там картинки и alt с примерами | — |
| Превью ссылок | `design/img/og/og-en.jpg`, `og-ru.jpg` | если на картинке время/пример | — |

## 3. Для ИИ
| Место | Файл | Что меняется |
|---|---|---|
| `/verbisto/llms.txt` | `design/stranicy/llms.txt` (копируется сборкой) | строка «Tenses: …the set is growing»; «Who it's for / Not for»; цены US с оговоркой; строка про RU-страницу |
| Корневой llms.txt | `~/itoroapps-site/docs/llms.txt` (правится руками, файл общий с léxito) | абзац Verbisto: пять мест, «≠ Verbito / Verbizo / Verbooster» |
| JSON-LD | `design/instrumenty/sobrat.py` (собирает из description и FAQ) | руками — только `operatingSystem` (iOS 26) и `offers` |
| sitemap | `sobrat.py` + `~/itoroapps-site/docs/sitemap.xml` | только при новых адресах; затем IndexNow (ключ `docs/verbisto/9383…txt`) и GSC |

## 4. App Store (ведёт координатор)
| Место | Файл | Что меняется |
|---|---|---|
| Подзаголовок EN/RU | `~/Conjugador/design/vitrina/metadata.json` → `en-US.subtitle`, `ru.subtitle` | обычно нет |
| Ключевые слова | там же, `keywords` | **сейчас перечисляют времена** (preterite, imperfect, pluperfect, perfect / indefinido, perfecto, imperfecto) — добавить новое (present / presente, subjunctive, condicional) |
| Промо и описание | `promotionalText`, `description` | перечень времён и функций, если есть |
| What's New | `whatsNew` | новое время / функция |
| Покупки | `inAppPurchases.*.description` («All tenses / Все времена») | меняется, только если граница бесплатного другая |

## 5. Порядок при выходе нового
1. Сверить факт в коде (§1). 2. App Store (§4) — координатор. 3. Страницы EN → кадры → слово владельца → выкладка →
RU тем же порядком (§2). 4. llms.txt оба (§3). 5. Проверка `forbidden-claims` по сборке. 6. IndexNow + GSC.
7. Через неделю — Google AI Mode по запросам из разбора §11: появилось ли новое в ответах.
