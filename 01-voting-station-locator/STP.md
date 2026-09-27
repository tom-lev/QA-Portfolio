# Software Test Plan (STP) - Voting Station Locator

**System under test:** [gov.il - Voting Station Locator (איתור קלפי)](https://www.gov.il/apps/moin/bocharim/)

| Version | Author | Update Date | Reviewed by | Review Date |
|---|---|---|---|---|
| 1.0.0 | Tomer Levin | _TBD_ | Self-review (solo portfolio project, no external approver) | _TBD_ |

## Table of Contents

1. [Introduction](#1-introduction)
2. [Test Strategy](#2-test-strategy)
3. [Resources](#3-resources)
4. [Schedule & Milestones](#4-schedule--milestones)
5. [Test Deliverables](#5-test-deliverables)
6. [Risks & Assumptions](#6-risks--assumptions)
7. [Monitoring & Control](#7-monitoring--control)

## 1. Introduction

This document is the System Test Plan (STP) for the manual QA testing project of the gov.il Voting
Station Locator. It defines the test strategy, scope, risk management, required resources, schedule,
and entry/exit criteria for the test round.

This is a solo, self-directed portfolio project: one tester (Tomer Levin), no client, no development
team, and no ownership of the system under test. Several sections below that would normally describe
team coordination or client acceptance are marked **N/A** for that reason, with a short note on how the
equivalent activity is actually handled in this project.

The document covers testing of a single combined flow: voter eligibility check + polling station
lookup.

### 1.1 System Under Test Description

The Voting Station Locator ("איתור קלפי") is a page on gov.il that lets a citizen check voter
eligibility and find their assigned polling station by submitting their ID number and date of birth.

- **Linked content:** the page also links to a secondary page, "reasons for exclusion from the voter
  roll" (לסיבות אי הכללות בפנקס), covered under UI/UX scope ([2.1.3](#213-test-types-to-be-tested)).
- **Boundaries:** testing is limited to the public-facing eligibility-check + polling-station-lookup
  form and its immediate linked content. The SUT is a **live production government system not owned or
  controlled by the tester** - there is no server-side access, no ability to inspect or call an API
  directly, and no ability to fix or deploy changes.
- **Primary users:** unauthenticated citizen (single user type - no login, no registration, no admin
  role exposed to the public).
- **External interfaces:** Israel Population Registry (backend match against voter roll, incl. an
  age-eligibility check) - not directly observable or testable; inferred only from UI responses.

## 2. Test Strategy

### 2.1 Scope

#### 2.1.1 Functional requirements to be tested

| # | Name | Description |
|---|---|---|
| 1 | Data entry (הזנת פרטים) | Entering an ID number and a birth date, the form's only two fields. Covers ID field validation (digit count, check digit, format) and birth-date field validation (valid dates, invalid day-in-month combinations, leap-year edge cases, and the `00`-as-unknown-birthdate convention historically used in Israel's population registry - documented at [Hebrew Wikipedia](https://he.wikipedia.org/wiki/תאריך_לידה#קביעת_תאריך_הלידה); see [`exploration-notes.md`](exploration-notes.md) for full detail). |
| 2 | Form submission & registry match (שליחת הטופס ואיתור התאמה במרשם האוכלוסין) | Submitting the form and receiving the correct result: an eligible, matching voter gets their polling station details; a registered citizen under voting age gets the correct ineligibility message; non-matching submissions are handled correctly; a rapid double-click sends a single request; the browser back button resets the form cleanly. |

#### 2.1.2 Functional requirements NOT tested

| # | Item | Reason |
|---|---|---|
| 1 | Voter registry data accuracy (ground truth) | No access to the real voter roll to verify results against; only the tester's own fictitious or real test data can be checked. |

#### 2.1.3 Test types to be tested

Compatibility, Accessibility, Security (basic), and UI/UX below are not modeled in the functional
traceability matrix - they're tracked separately (test cases + results live in `test-scripts.md` /
`STR.md`).

| Test type | Scope for this project | # Testers |
|---|---|---|
| Functional | Field validation, form submission, result display - see [2.1.1](#211-functional-requirements-to-be-tested). | 1 |
| Compatibility | Leading desktop browsers (Chrome, Edge, Firefox, Safari, latest stable) and mobile/responsive layout, checked via browser DevTools device emulation and a personal smartphone. | 1 |
| Accessibility / keyboard navigation | Keyboard-only navigation of the form, logical Tab order, field labels, focus handling. | 1 |
| Security - basic | Input sanitization / injection attempts in the ID field (e.g. script tags), HTTPS enforcement, and checking that error messages don't enable user enumeration. | 1 |
| UI/UX - general | On-page navigation/links (e.g. the "reasons for exclusion" link and its own links), clarity of error messages, visual consistency. | 1 |

#### 2.1.4 Test types NOT tested

| Test type | Reason |
|---|---|
| Performance / Load | The SUT is a live production government system not owned by the tester - there is no authorization or safe way to generate artificial load against it. |
| API | No documented or accessible public API. |
| Advanced security (penetration testing) | Would require explicit authorization from the system owner. |
| Reliability | Requires inducing failure and inspecting recovery at the infrastructure level - access the tester doesn't have on someone else's live production system. |
| Portability | Requires migrating the system between environments - the tester has no access to its deployment or infrastructure, only the public URL. |

#### 2.1.5 Regression Testing

This project is planned as a single initial test round. No regression testing is performed within this
round.

Because the tester does not control the SUT and there is no release/changelog access for an external
live government site, "regression" in a future round would mean re-running the full functional suite
whenever the live site is observed to have visibly changed (e.g. ahead of the next election cycle),
rather than regression tied to a specific code release.

#### 2.1.6 Bug-fix Verification Testing - **N/A**

Not applicable in this project. The SUT is an external live government system with no development team
or bug tracker on the tester's side to submit fixes against, so there is no fix → re-verify → close
workflow to run. Any bugs found during execution are documented as final artifacts in `bug-reports.md`
(with repro steps and evidence) as a demonstration of bug reporting practice, not as inputs to an active
fix cycle.

#### 2.1.7 Exit Criteria - Test Execution

| Exit criterion | Target |
|---|---|
| % of requirements covered by test cases | 100% |
| % of planned test cases executed | 100% of the test cases for which suitable test data can be obtained (see the data-access constraint under [Risks](#6-risks--assumptions)) |
| % of executed test cases passed | 90% |
| Test cases left unexecuted without a documented reason | 0 |
| Bugs found written up in `bug-reports.md` with repro steps and evidence | 100% |
| `STR.md` completed summarizing results | Yes |

#### 2.1.8 Exit Criteria - Acceptance Testing - **N/A**

Not applicable. This is a solo portfolio project with no client or stakeholder to run a formal
acceptance phase with; `STR.md` serves as the final sign-off artifact instead.

#### 2.1.9 Suspension Criteria

| Criterion | Trigger |
|---|---|
| Test environment unavailable | The live site is down, blocked by Cloudflare, or mid-redesign - pause until it's usable again. |
| Basic sanity fails | The form fails to load or cannot be submitted at all - pause and investigate before continuing. |

No team/PM escalation applies (solo project) - the tester decides when to resume.

### 2.2 Severity & Priority Definitions

Used to classify bugs in `bug-reports.md`.

**Severity** (impact of the defect on the system):

| Severity | Definition |
|---|---|
| Critical / Blocker | Breaks the core flow entirely - e.g. the form cannot be submitted, or a valid eligible voter cannot get a result, with no workaround. |
| High | Significant impact on the core flow's correctness (e.g. an invalid value is silently accepted and produces a misleading result), but a workaround exists. |
| Medium | Secondary functional issue or minor logic error not on the critical path. |
| Low | Cosmetic issues - copy/spelling, visual/layout polish only. |

**Priority** (urgency of fixing, independent of severity; used here for classification/reporting
practice, since the tester cannot actually schedule fixes on this external system):

| Priority | Definition |
|---|---|
| P1 | Should be fixed immediately if this were an owned system. |
| P2 | Should be fixed before the next release. |
| P3 | Fix when convenient. |
| P4 | Cosmetic / nice to have. |

## 3. Resources

### 3.1 Test Environment

Functional, compatibility, accessibility, and basic-security testing all share the same environment in
this project.

- **Client side:** personal computer with internet connection and browser(s) (Chrome, Edge, Firefox,
  Safari where available); a personal smartphone and/or browser DevTools device emulation for
  responsive/mobile checks; browser DevTools for basic security/network inspection.
- **Server side:** **N/A** - the SUT is gov.il's live production environment. It is external and not
  controlled or observed by the tester; there is no lower/QA environment available to test against, so
  all testing is performed carefully and non-destructively against production.

### 3.2 Equipment & Infrastructure

| Equipment | Quantity | Reason |
|---|---|---|
| Personal computer + browsers (Chrome, Edge, Firefox, Safari where available) | 1 | Functional, compatibility, and UI/UX testing. |
| Smartphone or browser DevTools device emulation | 1 | Responsive/compatibility checks. |
| Browser DevTools (built-in) | 1 | Basic security checks (network/requests, HTTPS enforcement) and accessibility checks. |

No dedicated paid tooling (e.g. load-testing, mobile device farms, security scanners) is used - out of
scope per [2.1.4](#214-test-types-not-tested).

### 3.3 Effort & Headcount Estimate

| Activity | Size (# test cases) | Est. effort (hours) | # Testers |
|---|---|---|---|
| Requirements / exploratory analysis | _TBD_ | _TBD_ | 1 |
| Test round 1 (scripting + execution) | _TBD_ - to be sized once the traceability matrix is finalized | _TBD_ | 1 |

## 4. Schedule & Milestones

| Activity | From | To | Duration (days) |
|---|---|---|---|
| Requirements / exploratory analysis | 2026-09-20 | 2026-09-27 | 7 |
| Test round 1 (scripting + execution) | 2026-09-29 | 2026-10-10 | 12 |
| Reporting (STR) | 2026-10-11 | 2026-10-14 | 4 |

## 5. Test Deliverables

| Deliverable | Planned submission date | Review date |
|---|---|---|
| `STP.md` | 2026-09-27 | 2026-09-29 |
| Traceability matrix (Google Sheets) | 2026-09-27 | 2026-09-29 |
| `test-scripts.md` | 2026-10-10 | 2026-10-12 |
| `run-report.md` | 2026-10-10 | 2026-10-12 |
| `bug-reports.md` | 2026-10-10 | 2026-10-12 |
| `STR.md` | 2026-10-14 | 2026-10-16 |

## 6. Risks & Assumptions

### General risks (anticipated for this type of system)

| # | Risk / Assumption | Mitigation |
|---|---|---|
| 1 | Cloudflare bot management may flag or block repeated/rapid manual testing sessions, since this is a public production system. | Pace testing manually across sessions; avoid any automation or rapid repeated submissions. |
| 2 | Full eligibility/match scenarios require real personal data (the tester's own, or a real registered citizen's) to produce an actual registry match, which raises privacy-handling requirements for test data. | Real values are never recorded in this repo (code, docs, or screenshots) - only the test result is documented. Wherever a real match isn't required, fictitious ID numbers with a valid check digit are used instead (see [`exploration-notes.md`](exploration-notes.md) for the check-digit algorithm). |
| 3 | Some edge-case scenarios (e.g. a citizen at a specific age boundary) may require the real registry data of a specific citizen the tester has no access to and cannot fabricate, since a genuine registry match is required. Such cases may turn out not to be executable this round. | If no suitable test data can be found for a given case, mark it Not Executed in `run-report.md` with the reason stated, rather than counting it against the pass-rate exit criterion (see [2.1.7](#217-exit-criteria---test-execution)). |
| 4 | The live site is external production infrastructure outside the tester's control and may change (redesign, copy, validation logic) mid-round. | Record the date/screenshot evidence for every test case executed, so a mid-round change is visible and re-testable rather than silently invalidating prior results. |

### Risks identified during exploratory testing (see [`exploration-notes.md`](exploration-notes.md))

| # | Risk / Assumption | Mitigation |
|---|---|---|
| 1 | The date dropdowns may allow selecting a day that doesn't exist in the selected month (e.g. day 31 with month 2), with no inline validation feedback. | Design test cases to systematically check invalid day-in-month combinations; if confirmed as a defect, document it fully in `bug-reports.md` with evidence. |
| 2 | The system may return the same generic error message regardless of whether the cause is a structurally invalid date or a valid-but-non-matching value, which would make results hard to diagnose. | Design test cases so each "no match" result can be cross-checked against a known-invalid vs. known-fictitious-but-valid input, to separate the two causes. |
| 3 | Inline validation behavior appears inconsistent between fields (present for the ID field, absent for the date fields). | Verify explicitly during birth-date entry testing; document as a UX consistency finding if confirmed. |
| 4 | `00` as day and/or month is a historical convention used in Israel's population registry (~800,000 people registered with `00.00` before ~2011), but it is not yet known how the system handles *partial* `00` combinations vs. the full `00.00` pair. | Design birth-date test cases to cover the full `00.00` case and each partial-`00` variant separately, and record the system's actual behavior for each. |

## 7. Monitoring & Control

### 7.1 Team status meetings - **N/A**

Not applicable - this is a solo project with no team to synchronize with. Progress is tracked directly
between work sessions via `run-report.md` and `test-scripts.md`.

### 7.2 Bug triage meetings - **N/A**

Not applicable - the SUT has no development team or bug tracker on the tester's side to triage defects
against. Found defects are written up directly in `bug-reports.md` as final deliverables (see
[2.1.6](#216-bug-fix-verification-testing---na)), using the severity/priority definitions in
[2.2](#22-severity--priority-definitions).

### 7.3 Progress Tracking Metrics (self-tracked)

| Metric | Description | Frequency | Target |
|---|---|---|---|
| Test case authoring progress | % of planned test cases scripted (in `test-scripts.md`). | Per work session | 100% before execution begins |
| Test environment readiness | Site reachable, form loads, no Cloudflare block. | Start of each session | Ready before executing |
| Requirements coverage | % of requirements covered by at least one test case. | Per work session | 100% |
| Execution status (Passed/Failed/Blocked) | Count and % of planned test cases executed, split by outcome. | Per work session | 95%+ of non-Blocked cases executed by round end |
