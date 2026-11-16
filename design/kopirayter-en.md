# EN landing — copywriter notes (variant-B-en.html)

Source: `variant-B-kopirayter.html` (RU, approved structure). Markup, classes, CSS and hero animation are identical
(checked by diff); only words, `lang`, links and the badge changed. Draft for the methodologist.

## Decisions
- **British spelling** (practise as a verb, telling-off, one-off, single quotes as in the app's EN rule texts).
  The audience learns Spain's Spanish, many are in the UK/Europe. The app catalog itself mixes (practice ×30, practise ×4).
- **"the app" / "Vosotros", never "the trainer"**: "trainer" reads as a shoe or a coach in English.
- **"accent"**, not "stress mark" or "written accent": it's the app's word in every verdict.
- Dashes: spaced em dash, as in the app's EN content quoted on the page. Copy uses curly apostrophes; the verbatim
  `introContrast.en` quote keeps its straight quotes.
- **"In your language"** leads with the English explanation; the Russian one follows, captioned "For Russian speakers,
  for comparison". The lead tells an English reader what the Russian box is about (verb aspect), since they can't read it.
- Vosotros paragraph speaks to the typical English learner: "if your course skipped vosotros, it isn't skipped here".
- Progress FAQ: no "paid tenses". "It all stays on your iPhone. If you subscribe again, you carry on where you left off."
- Cancel path: "Settings → Apple Account → Subscriptions" — Apple renamed Apple ID to Apple Account; same path as the
  app's paywall string (branch `claude/op-3-s-71300f`).
- H2 "Как платить" → **"Plans"** (no prices on the page, so not "Pricing").
- Footer trademark line: Apple's standard wording (Apple/Apple logo trademarks; App Store service mark).

## H1 and subhead
- Chosen H1: **Where's the mistake?** — a direct question the animation answers.
  Alternatives: "Spot the mistake." (classic classroom format) · "Can you see what's wrong?" · "What's wrong with comereis?"
- Chosen subhead: "Vosotros shows you which part of the verb went wrong and explains the rule."
  Alternatives: "See which part of the verb you got wrong — stem, ending or accent — and get the rule for it." ·
  "Type the form. See where it went wrong. Read the rule."

## App strings used verbatim (checked)
`Localizable.xcstrings` (master): The accent is missing. · The stem is off. · The ending is off. · The accent is off. ·
Infinitive · Ending · Tap a vowel to put the accent on it.
`zone_rules.json` → `futuro.ending.all.accent` en, first two sentences (third, about oír/reír, dropped as in RU).
`imperfecto.json` → `introContrast.en` and `.ru`, verbatim.
Plan names: **Yearly · Monthly · Lifetime** — catalog key `Forever` → en "Lifetime", ru "Навсегда"; only on branch
`claude/op-3-s-71300f`, not on master.

## To verify
1. **Lifetime**: the catalog says "Lifetime", but `Conjugador.storekit` has displayName **"Forever"** (en_US) and the
   paywall code key is "Forever". The App Store will show the App Store Connect name — make them one word.
2. "Examples" label (`.cap`) and "Back for review" — site wording; the catalog only has "Example" (singular).
   Check what the review screen actually shows.
3. Screenshot `img/razbor-osnova-ru.png` is the Russian interface. The EN page needs an English shot of the same screen;
   the alt text currently says "in the Russian interface". Once replaced, quote the EN rule text in the alt.
4. Rule on that screen: I assumed `indefinido.stem.orthography` (yo-only spelling change; examples buscaste, tocaste).
   Confirm, since the shot text says the app "marks the stem, explains the rule and shows forms built the same way".
5. "If your course skipped vosotros" — fair generalisation for Latin-American-based courses; methodologist to approve.
6. "Neither is a translation of the other ... starts from what their language already gives them" — same claim as RU.
7. Badge: only `app-store-en-us.svg` exists in `badges/`; no en-gb. Apple's US badge is fine for UK use, but check.
8. Trial reminder: "We'll remind you 2 days before they end" — matches the paywall string "We will remind you %lld days
   before it ends" (trialReminderDaysBefore = 2 assumed from HANDOFF).
9. Privacy/Support links are still `#` (pages not built yet).
