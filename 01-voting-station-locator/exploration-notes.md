# Exploration Notes — Voting Station Locator

Working notes from initial exploratory testing. To be used as input for
`functional-decomposition.md`, `STP.md`, `test-cases.md`, and `bug-reports/`.
Not a final deliverable — raw findings only.

## System basics

- URL: https://www.gov.il/apps/moin/bocharim/
- Angular SPA (Angular Material), protected by Cloudflare bot management.
  Raw HTML is an empty shell (`<app-root>`) — content renders client-side only.
- Google Analytics (GA4) installed.
- Main screen title: "מודיעין בחירות | איתור קלפי"
- Subtitle: "בדיקת זכאות לבחור ומיקום הצבעה בבחירות לכנסת ה-26"
- Election date shown on page: Tuesday, 27 Oct 2026 (ט"ז בחשוון התשפ"ז)
- Voter roll snapshot date shown: 31/05/2026, with a link "לסיבות אי הכללות
  בפנקס" (reasons for exclusion from the voter roll) — not yet explored.

## Functional scope observed so far (for functional-decomposition.md)

- Voter eligibility check (combined with polling station lookup — not two
  separate features)
- Polling station locator (address + station number)
- Link/page: reasons for exclusion from the voter roll (not yet explored)
- Main form fields: תעודת זהות (9 digits), תאריך לידה (day/month/year
  dropdowns)

## Findings

### Confirmed bug — day dropdown not filtered by selected month
Day dropdown always offers 1–31 regardless of the selected month (e.g. 31 is
selectable with month = 02). No inline validation error appears when an
impossible date (e.g. 31/02) is selected. Submitting returns the same generic
"couldn't find your details" message as any non-matching input — the UI gives
no indication the date itself was invalid.
Evidence: `evidence/bug01-day-dropdown-shows-31-in-february.jpeg`,
`evidence/bug01-feb-31-selected.jpeg`
**Status: still considered a real bug** — to be written up formally.

### Investigated, reclassified as NOT a bug — "00" in day/month
Initially looked like a bug (00 is selectable in both day and month
dropdowns). Research confirmed this matches a real, documented convention:
until ~2011, ~800,000 immigrants without an official birth certificate were
registered in Israel's Population Registry with "00.00" as day/month of
birth. So 00/00 as a valid day+month combination is very likely intentional,
not a defect.
Evidence: `evidence/bug02-day-month-00-selected.jpeg`,
`evidence/bug02-invalid-date-generic-error.jpeg`
Source: https://www.nevo.co.il/law_html/law00/72938.htm ,
https://he.wikipedia.org/wiki/תאריך_לידה

**Open question — not yet tested:** does the system accept *partial* 00
combinations (day=00 with a real month, or a real day with month=00), or only
the full 00/00 pair? If only the full pair is a legitimate registry value,
partial combinations may still be an unhandled edge case worth a bug report.

### Investigated, likely NOT a bug — max selectable birth year is 2011
Initially looked suspicious (someone born in 2011 can't be 18 by the
2026-10-27 election). Research confirmed ID cards become mandatory at age 16
in Israel, and minors can voluntarily hold one younger than that. Best
hypothesis: this field only checks "does this ID + birthdate match a real
registry record" — actual voting-age eligibility (18) is most likely enforced
separately, after a match is found. All our test submissions used fictitious
IDs with no registry match, so we have not yet seen what happens after an
actual match (age-eligibility message, if any).
Source: https://www.kolzchut.org.il/he/קבלת_תעודת_זהות ,
https://teen.kolzchut.org.il/he/זכות:הוצאת_תעודת_זהות

### Positive finding — no user enumeration via error messages
Both "ID format invalid" (checksum fails) and "valid format but no match"
produce different messages, but neither confirms/denies whether a specific ID
number exists in the system in a way that would let someone enumerate valid
IDs. Worth documenting as a passing security/privacy-related test case.
Evidence: `evidence/positive-invalid-id-format-error.jpeg` (format error,
inline, red border, appears before/without submitting)
vs `evidence/bug02-invalid-date-generic-error.jpeg` (generic "not found",
appears after submitting)

### Investigated, likely NOT a bug — earliest selectable birth year is 1906
2026 (current year) − 1906 = exactly 120. Very likely a generic "maximum
plausible human age" cutoff (~120, close to the oldest verified person in
history, ~122), a common convention for birth-year fields — not necessarily
tied to Israel-specific history.
**Open question:** is this computed dynamically (`currentYear - 120`) or a
value hardcoded once? If hardcoded, it will quietly become wrong in future
years (blocking real 121+-year-old users). Cannot verify from the UI alone —
would need to re-check in a year, or inspect source/ask.

Real-world check: the oldest living person in Israel as of this writing is
Tzila Cohen, born 20/11/1914 (~110–111) — comfortably within the current
1906 cutoff (~8 years of margin). So this is **not an active bug today**, but
with rising life expectancy the margin will keep shrinking — worth
monitoring over time, especially if the value turns out to be hardcoded
rather than dynamic.
Source: https://www.ice.co.il/local-news/news/article/1088466

### Positive finding, flagged inconsistency — inline validation only on ID field
The ID field validates format inline (red border + message) seemingly on
blur/type, before submission. The date fields have no equivalent inline
validation for impossible values. Worth noting as a UX consistency
observation alongside the day/month bug above.

## Test ID numbers (fictitious, checksum-valid, safe to reuse — not real people)

Israeli ID checksum: multiply digits 1–8 alternately by 1/2 (left to right),
digit-sum any two-digit product, sum all 8 results, check digit = amount
needed to reach the next multiple of 10.

- 858224124
- 149426033
- 033568866
- 995292232
- 369138102

Note: 311170369 appears to be a pre-filled/placeholder ID shown by the site
itself in the ID field (matches a valid checksum) — not something we typed.
Worth double-checking this on a fresh page load.

## Still to test / open items

- [ ] Partial 00 combinations: day=00 + real month, real day + month=00
- [ ] Submit with a year near/above 2011 boundary (e.g. 2010, 2011, 2012) and
      compare responses
- [ ] What the "reasons for exclusion from the voter roll" link/page covers
- [ ] Behavior on mobile / responsive layout
- [ ] Keyboard-only navigation / basic accessibility of the dropdowns
- [ ] Other invalid-day-in-month cases beyond February (e.g. 31 in April,
      June, September, November)
- [ ] Re-check the earliest selectable year (currently 1906) after some time
      has passed, to see if it moves with the current year (dynamic) or stays
      fixed (hardcoded, future bug)
