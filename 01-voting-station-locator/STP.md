# Software Test Plan (STP) — Voting Station Locator

_TBD_

## 1. Objective

## 2. Scope
### In Scope
- Functional testing (field validation, form submission, result display)
- Compatibility testing (cross-browser / cross-device) — non-functional
  (ISTQB / ISO 25010 quality characteristic), in scope for this project but
  **not** modeled in the functional traceability matrix (Requirement → Test
  Condition → Test Case). Tracked separately (test cases + results live
  outside that matrix, e.g. in `test-scripts.md` / `STR.md`).
- Accessibility / keyboard navigation — non-functional (Usability/
  Accessibility, ISO 25010), same treatment as Compatibility above: in scope
  for this project, not part of the functional traceability matrix, test
  cases + results tracked separately. Planning and execution still to come.
- Security (basic) — non-functional (Security, ISO 25010), same treatment as
  above: input sanitization / injection attempts (e.g. script tags in the ID
  field), basic transport checks (HTTPS enforced). Not part of the
  functional traceability matrix. Planning and execution still to come.
- UI/UX (general) — non-functional (Usability), same treatment as above.
  Covers things like on-page navigation/links working correctly (e.g. the
  "reasons for exclusion from the voter roll" link and its own links) —
  checked as part of a general UI/UX pass, not modeled as its own functional
  requirement. Planning and execution still to come.

### Out of Scope
- **Network reliability / fault injection** (slow or dropped connection during
  form submission) — this is non-functional (Reliability), not functional.
  Noted as a candidate for a future dedicated non-functional/performance
  effort (see portfolio TODO, project 10), not executed as part of this
  project's functional test cases.

## 3. Test Approach

## 4. Test Environments

## 5. Entry Criteria

## 6. Exit Criteria

## 7. Severity & Priority Definitions

## 8. Risks & Assumptions
- **Test data & privacy:** one test case (matching a real registered voter)
  requires the tester's own real ID number and date of birth. These real
  values are never recorded in this repo (code, docs, or screenshots) — only
  the test result is documented. All other test cases use fictitious,
  checksum-valid ID numbers that do not belong to real people. See
  `exploration-notes.md` for the Israeli ID checksum algorithm used to
  generate these fictitious values.

## 9. Schedule
