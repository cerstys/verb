# E9 EN: тексты лендинга (dvizhenie-E9-en.html)

Орфография британская, как в старой версии (practise как глагол). Кавычки типографские (’ “ ” ‘ ’).

## Заголовки и ключевые фразы: RU → EN
- title: Verbisto — тренажёр испанских глаголов для iPhone → Verbisto — Spanish verb practice for iPhone
- кикер: …· испанский Испании → Spanish verb practice for iPhone · Spanish from Spain
- H1: Где здесь ошибка? → Where’s the mistake?
- вердикт героя: Нет знака. → The accent is missing.
- подписи частей: Инфинитив / Основа / Окончание → Infinitive / Stem / Ending
- кнопки героя: Показать / Почему так? / Ещё пример → Show / Why? / Another one
- подзаголовок → The app shows you which part of the form is wrong, and explains the rule.
- строка под значком → No need to pay up front: Indefinido and Perfecto are free forever, and on the yearly plan the full version is free for the first 7 days.
- H2: Форму набираете вы. → You type it.
- три места → There are three places to go wrong. The app tells you which one.
- вердикты карточек: Основа — не та. / Окончание — не то. / Знак здесь не нужен. → The stem is off. / The ending is off. / No accent here.
- H2: Тренажёр разбирает. → The app breaks it down.
- лид → Not a lecture on the whole tense. One rule, about the mistake you made, plus two examples.
- рассказ: Видно, где и почему. → See where, and why.; Никаких очков и упрёков. → No points. No telling-off.
- H2: На вашем языке. → In your language.
- подписи: Для русскоговорящих / Для англоговорящих → For Russian speakers / For English speakers
- H2: Трудное возвращается. → The hard ones come back.
- подпись очереди: Вернулись к повторению → Back for review
- H2 цен: Сначала <em>занятия.</em> Оплата — потом. → <em>Practise</em> first. Pay later.
- под ним: …первая неделя — ваша. → No need to pay up front: on the yearly plan, the first week is free.
- тарифы: Месяц / Год / Навсегда → Monthly / Yearly / Lifetime
- листки: СЕГОДНЯ · 1 из 7 бесплатных дней / ДЕНЬ 6 · НАПОМНИМ / ДЕНЬ 8 · ОПЛАТА → TODAY · 1 of 7 free days / DAY 6 · REMINDER / DAY 8 · PAYMENT
- Год: Неделя — бесплатно, вся полная версия… → The first week is free, full version included. Then one payment a year.
- H2: Подойдёт ли вам → Is it for you?; Подойдёт, если / Не подойдёт, если → It’s for you if / It’s not for you if
- H2: Вопросы → Questions
- FAQ 1: Можно ли сначала позаниматься бесплатно? → Can I practise for free first? (…we’ll remind you 2 days before you pay)
- концовка → Learning the Spanish spoken in Spain? Here you practise vosotros just like every other person.
- подвал: Конфиденциальность · Поддержка · Условия → Privacy · Support · Terms

## Где сознательно отошёл от буквы
1. «Первая неделя — ваша» → «the first week is free». «Is yours» по-английски звучит как рекламный оборот без содержания; «free» прямо снимает страх списания, как просит рамка.
2. Пример для русскоговорящих: «вчера мы поиграли» и «два года я жил» англоязычному ничего не скажут сами по себе, поэтому в текст добавлено, что в русском глагол совершенного/несовершенного вида (perfective / imperfective). Без этого блок не показывает, что русским объясняют через вид.
3. «Форму набираете вы.» → «You type it.» (из старой версии). Короткий английский заголовок сильнее, чем «You type the form».
4. «Никаких очков и упрёков» → «No points. No telling-off.» Две короткие фразы вместо «no points or reproaches»: «reproach» в английском книжное.
5. aria-label экрана разбора: вместо цитаты вердикта «Основа — не та.» написано «the stem is marked as wrong». На кадре (razbor-osnova-ru-3x.jpg) русский текст, и английская цитата была бы неправдой о картинке. Сам кадр на английской странице русский: нужна английская версия кадра (вне моей задачи).
6. Вердикт «Нет знака.» → «The accent is missing.» Голое «No accent.» читается как «акцент не нужен» и спорит с карточкой «No accent here.»

## Мелкая правка разметки
FAQ «Какие времена»: русское «и» стояло внутри `<span lang="es">`. Теперь `…Pluscuamperfecto</span> and <span lang="es">Futuro Simple</span>`, чтобы английское «and» не было размечено как испанское.

## Проверка кириллицы
- Вне HTML-, CSS- и JS-комментариев: **0 строк**.
- Всего строк с кириллицей в файле (`grep -c '[А-Яа-яЁё]'`): 65, все они комментарии, их не трогал.
