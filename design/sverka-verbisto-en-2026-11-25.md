# Сверка EN-страницы Verbisto перед выкладкой (25.11.2026)

Страница: сборка `itoroapps-site` e37c0c8 / исходник `verb` 97b8df6. Источники: разбор `design/razbor-smyslov-2026-11-25.md`
§5 (боли и ответы продукта), §11 (реальные запросы, Google AI Mode); `Conjugador/landing/forbidden-claims.txt`;
код `Conjugador/Engines/MissLocation.swift:44` (Zone), `EngineConfig.swift:13` (freeTenseIds), `:17` (trialReminderDaysBefore).

## Боли (§5, §11)
| Боль (их словами) | На странице | Что поправить |
|---|---|---|
| Правила знаю, а форму не выдаю | есть: «You know what the Indefinido (the preterite)… but the forms still trip you up» | — |
| Ставит ошибку и не говорит почему | есть: строка над H1 (пять мест), «For each mistake, it explains the rule for that exact spot» | — |
| Preterite и imperfect сливаются (EN «preterite vs imperfect», RU «indefinido и imperfecto разница» № 1) | есть: FAQ + блок «Written for English speakers»; режим не обещан | — |
| Курс без vosotros, еду в Испанию («does duolingo teach vosotros») | есть: «your course skipped vosotros», «Vosotros isn’t skipped here» | Duolingo по имени не названо — сознательно |
| Одно ударение — и «неверно» | есть: FAQ «I left out one accent…» | — |
| Неправильные во futuro не держатся | частично: «irregular verbs included», «The hard ones come back» | — |
| Звук, навязчивые уведомления | есть: FAQ «Will it nag me…» | — |
| Подписка без разовой | есть: Lifetime | — |

## Люди
| Пункт | Есть? | Что поправить |
|---|---|---|
| GCSE / A-level (слово «revision») | да — блок «Is it for you?» + FAQ | — |
| DELE A2 для гражданства (CCSE растёт) | да — блок + FAQ, честно «не весь экзамен и не CCSE» | — |
| Переезд в Испанию | да | — |
| «Не для вас» без отталкивания presente | да (presente не упомянут) | — |
| Путь первого экрана | строка (что + чем отличается) → H1 → живой пример → строка про правило → кнопка App Store → «бесплатно навсегда» | на первом экране нет слова «iPhone» (было в прежней строке); есть в title, кнопке, FAQ — оставить |
| «Для кого» — вторым экраном | да | — |

## ИИ и поиск
| Пункт | Есть? | Что поправить |
|---|---|---|
| title со словами поиска | да: «Spanish verb conjugation practice for Spain (vosotros included) · iPhone» | — |
| description = определение «что, чем отличается» | да, с пятью местами; в JSON-LD MobileApplication тот же текст | — |
| FAQPage в разметке | да, 15 вопросов, сверено со страницей сборкой | — |
| Ответ на запросы, где AI Mode советует Ella Verbs («explains why wrong»), ConjuGato («vosotros toggle»), GCSE | да: конкретика (пять мест, отметка на буквах, ответ не показывает, ударение — отдельный вердикт, vosotros без переключателя), GCSE/DELE в FAQ | — |
| «Verbisto ≠ Verbito / Verbizo / Verbooster» | в обоих llms.txt — да; на странице — нет | вынести на страницу — новое, не делал (по умолчанию: не надо, хватает llms.txt и title с «Verbisto») |
| llms.txt | пять мест, «для кого / не для», времена без перечня, цены US с оговоркой | — |
| Слова поиска «conjugation», «preterite», «practice», «revision», «vosotros», «Spain» | все есть (было 0 «conjugation» и 0 «preterite») | — |
| Анимированные слова для машин | целое слово скрытым текстом, буквы `aria-hidden` | — |

## Факты и рамки
| Пункт | Есть? | Что поправить |
|---|---|---|
| Пять мест = `MissLocation.Zone` (accent, auxiliary, stem, ending, participle) | совпадает | — |
| Бесплатно навсегда = `freeTenseIds` ["indefinido","perfecto"] | совпадает | — |
| Напоминание за 2 дня до оплаты = `trialReminderDaysBefore 2`; «день 6 из 7, оплата в день 8» | совпадает | — |
| forbidden-claims | **было нарушение (старое, до правок 25.11): «works offline»** на странице (FAQ) и в llms.txt | **поправлено** (97b8df6 / e37c0c8): «Not for practice. You need a connection…», «Practice needs no internet connection…». Теперь 0 совпадений |
| Перечень времён не писать | на странице нет; в llms.txt «past tenses… and the future for now; the set is growing» | — |
| Цены на странице не ставить | нет (только «Prices are in the App Store») | — |
| Режим сравнения не упоминать | нет | — |

Вынести на решение (не блокирует выкладку): «Verbisto ≠ Verbito» на самой странице — по умолчанию не делать.
