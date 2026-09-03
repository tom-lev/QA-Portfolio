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
  outside that matrix, e.g. in `test-cases.md` / `STR.md`).

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
  checksum-valid ID numbers that do not belong to real people.

## 9. Schedule
