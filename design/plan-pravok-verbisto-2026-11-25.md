# План правок страницы Verbisto (EN, затем RU) — на «да» владельца

25.11.2026. Основа: `design/razbor-smyslov-2026-11-25.md` (§5 — смыслы, §11 — реальные запросы).
Рамки: цен на странице нет; числа глаголов и перечня времён нет; режим сравнения не упоминаем;
`Conjugador/landing/forbidden-claims.txt` (нет «only app», «works offline» как отличия, «scientifically»,
«remember forever»). Вид страницы не меняется, кроме новых строк текста и порядка блоков (п. 4).

## Почему (три факта из поиска)
1. **ИИ не знает Verbisto**: Google AI Mode на «Verbisto Spanish verbs app review» отвечает «такого нет» и
   предлагает Verbito / Verbizo / Verbooster. В App Store по имени «verbisto» приложение не находится (US, GB).
2. **На EN-странице нет главных слов поиска**: «conjugation» — 0 раз, «preterite» — 0 раз. Люди ищут
   «spanish conjugation practice app», «preterite vs imperfect», «gcse spanish verb practice».
3. **«Explains why you're wrong» уже говорит Ella Verbs** (ИИ советует её именно за это, она растёт в UK).
   Наше отличие надо называть конкретно, а не общими словами.

## Правки (каждая — отдельно на «да»)

**1. title и description**
- title: `Verbisto — Spanish verb conjugation practice for Spain (vosotros included) · iPhone`
  (сейчас: «Verbisto — Spanish verb practice for iPhone»).
- description: *Verbisto is an iPhone app for Spanish verb conjugation practice, Spanish from Spain with vosotros.
  You type each form; it marks the exact letters that went wrong (stem, ending, accent or helper verb) and explains
  the rule for that spot.*

**2. Строка смысла над «Where's the mistake?»** (H1 оставить — крючок анимации). На выбор:
- A: *Spanish verb conjugation practice for the Spanish of Spain — and exactly where your form went wrong.*
- B: *Know the rules but still get the forms wrong? Verbisto shows which part is off: stem, ending or accent.*

**3. Отличие — конкретно** (одна строка в блоке «The app breaks it down», черновик):
*It marks the letters you got wrong and doesn't type the answer for you while you still have tries. A missing
accent isn't marked as a wrong answer — it's its own verdict, and the app shows why the mark changes the word
(hablo / habló).*

**4. «Is it for you?» — выше, вторым экраном, с людьми**
- It's for you if: revising Spanish verbs for **GCSE or A-level** (past tenses and the future); preparing **DELE A2
  for Spanish citizenship**; **moving to Spain** and your course skipped vosotros; you know the rules but the forms
  still trip you up; you'd rather type than pick from a list.
- Not for you if: just starting; Latin American Spanish is your goal; you need the present tense or the
  subjunctive right now; speaking practice; Android.

**5. Слова поиска в тексте**: при первом упоминании — *Indefinido (the preterite)*, *Imperfecto (the imperfect)*;
одно естественное «conjugation» в первом экране и в FAQ.

**6. FAQ — новые вопросы** (их словами; в FAQPage):
- *I keep mixing up the preterite and the imperfect. Will this help?* — опора на готовый текст про английское
  «played»; про режим сравнения — ни слова.
- *Is it good for GCSE or A-level Spanish revision?* — да для прошедших и будущего; настоящего пока нет.
- *I need DELE A2 for Spanish citizenship. Does it help?* — тренирует формы прошедших и будущего, не весь экзамен
  и не CCSE.
- *Is it Spain Spanish or Latin American?* — Испания: vosotros всегда, perfecto для «сегодня».
- *I left out one accent. Is my answer wrong?* — отдельный вердикт, не «неверно».
- *Will it nag me or make noise?* — звука нет; одно тихое напоминание в день по желанию.
- Explanations: «English and Russian» (если на EN-странице уместно — решает владелец).

**7. Правка существующего FAQ «Which tenses does it cover?»** — сейчас перечисляет пять времён, а слово
владельца 25.11 — перечень не писать. Предложение: *The past tenses and the future for now, and the set is
growing. Indefinido and Perfecto are free forever.*

**8. Текст для машин в анимированных словах** (`comereis` / `comeréis`): целое слово скрытым текстом,
буквы — `aria-hidden`. Вид не меняется.

**9. llms.txt (verbisto и корень)**: строка *Verbisto (by itoroapps; App Store id6836263523) is not Verbito,
Verbizo or Verbooster.* + те же слова поиска (conjugation practice, preterite). Цены там уже есть.

**10. Не трогать**: «No points. No telling-off.», «Written for English speakers», «Practise first. Pay later.».

## RU-страница (после EN, теми же пунктами)
- title: «Verbisto — тренажёр спряжения испанских глаголов Испании (с vosotros) · iPhone».
- «Объяснения на русском» — **не отличие** (есть у Lorito, Lingvity): не писать «нигде больше». Отличие — разбор
  формы по частям и Испания по умолчанию.
- Слова поиска: «спряжение испанских глаголов», «тренажёр», «indefinido и imperfecto — разница» (в FAQ без
  обещания режима).
- /verbisto/ru/ нет в индексе Google — после правки запросить индексацию в GSC.

## Вне страницы — координатору
- App Store: по имени «verbisto» не находится (US, GB); в GB по «vosotros» — № 8, в US нет. Проверить
  доступность в витринах и ключевые слова/подзаголовок в ASC (ведёт координатор).
- Gramanator (европейский испанский по умолчанию, iPhone с 12.10.2026) — новый конкурент на позиции
  «Испания по умолчанию».

## Порядок работы после «да»
EN-правки в `design/dvizhenie-E9-en.html` → сборка `sobrat.py` → кадры мобильный/десктоп, день/ночь →
показ владельцу → выкладка по слову → RU тем же порядком → IndexNow + запрос индексации.
