# Test Scripts - Voting Station Locator

Detailed step-by-step scripts for the test cases defined in the
[traceability matrix](https://docs.google.com/spreadsheets/d/1N10lbNpYWRBuHuPAgquC69JrYWB3VnxMGj2IGlV-TFM/edit?usp=sharing)
(source of truth for which test cases exist). `ID` below matches the TC
number from that matrix, such as `1.1.1` or `2.1.1`.

**Common preconditions** (unless a row states otherwise): browser open, navigate to
`https://www.gov.il/apps/moin/bocharim/`, the eligibility/locator form is loaded with the ID and birth
date fields empty.

**Privacy note:** rows that require the tester's own real ID number and birth date, or a real registered
citizen's data, never record the actual values here - only the field/step being exercised. See `STP.md`
Risks for the full rationale.

## Requirement 1.1 - ID number entry

| ID | Title | Preconditions | Steps | Expected Result |
|---|---|---|---|---|
| 1.1.1 | Valid 9-digit ID, valid check digit - 858224124 | Common preconditions | 1. Enter `858224124` in the ID field.<br>2. Do not submit yet - observe the field. | No inline error message; the field is accepted and the user can continue filling in the rest of the form. |
| 1.1.2 | Invalid 9-digit ID, invalid check digit - 858224127 | Common preconditions | 1. Enter `858224127` in the ID field.<br>2. Do not submit yet - observe the field. | An inline error message is shown for the ID field; the user cannot proceed as if the value were valid. |
| 1.1.3 | Invalid 8-digit ID - 85822412 | Common preconditions | 1. Enter `85822412` in the ID field.<br>2. Do not submit yet - observe the field. | An inline error message is shown for the ID field. |
| 1.1.4 | Invalid 10-digit ID - 8582241277 | Common preconditions | 1. Enter `8582241277` in the ID field.<br>2. Do not submit yet - observe the field. | An inline error message is shown for the ID field. |
| 1.1.5 | Invalid ID with non-numeric characters - 85822412% | Common preconditions | 1. Enter `85822412%` in the ID field.<br>2. Do not submit yet - observe the field. | An inline error message is shown for the ID field. |
| 1.1.6 | Empty ID field | Common preconditions | 1. Leave the ID field empty.<br>2. Select the valid, existing birth date `10.02.1994` so only the ID field is empty.<br>3. Attempt to submit the form. | An error/required-field indication is shown for the ID field specifically; the form does not submit. |

## Requirement 1.2 - Birth date entry (selecting from the dropdown)

| ID | Title | Preconditions | Steps | Expected Result |
|---|---|---|---|---|
| 1.2.1 | Select a real, existing date - 10.02.1994 | Common preconditions | 1. Enter ID `858224124`.<br>2. Select day `10`, month `02`, year `1994` from the dropdowns.<br>3. Do not submit yet - observe the date fields. | No inline error message; the fields are accepted and the user can continue. |
| 1.2.2 | Select a day that doesn't exist in the month - 31.4 | Common preconditions | 1. Enter ID `858224124`.<br>2. Select day `31`, month `4` (April) from the dropdowns.<br>3. Do not submit yet - observe the date fields. | An inline error message is shown, since day 31 doesn't exist in April. |
| 1.2.3 | Select a leap-year date - 29.02.2000 | Common preconditions | 1. Enter ID `858224124`.<br>2. Select day `29`, month `02`, year `2000` from the dropdowns.<br>3. Do not submit yet - observe the date fields. | No inline error message; 2000 is a leap year so 29 February is valid. |
| 1.2.4 | Upper boundary+1, February, leap year - 30.02.2000 | Common preconditions | 1. Enter ID `858224124`.<br>2. Select day `30`, month `02`, year `2000` from the dropdowns.<br>3. Do not submit yet - observe the date fields. | An inline error message is shown; February never has a 30th day, even in a leap year. |
| 1.2.5 | Upper boundary+1, February, non-leap year - 29.02.2025 | Common preconditions | 1. Enter ID `858224124`.<br>2. Select day `29`, month `02`, year `2025` from the dropdowns.<br>3. Do not submit yet - observe the date fields. | An inline error message is shown; 2025 is not a leap year so February only has 28 days. |
| 1.2.6 | Select the full unknown-date value - 00.00.0000 | Common preconditions | 1. Enter ID `858224124`.<br>2. Select day `00`, month `00`, year `0000` from the dropdowns.<br>3. Do not submit yet - observe the date fields. | No inline error message; `00.00.0000` is a documented convention for citizens without an official birth certificate (see `exploration-notes.md`). |
| 1.2.7 | Select a partial unknown date (month known) - 00.10.0000 | Common preconditions | 1. Enter ID `858224124`.<br>2. Select day `00`, month `10`, year `0000` from the dropdowns.<br>3. Do not submit yet - observe the date fields. | No inline error message. |
| 1.2.8 | Select a partial unknown date (day known) - 10.00.0000 | Common preconditions | 1. Enter ID `858224124`.<br>2. Select day `10`, month `00`, year `0000` from the dropdowns.<br>3. Do not submit yet - observe the date fields. | No inline error message. |
| 1.2.9 | Select a partial unknown date (year known) - 00.00.1994 | Common preconditions | 1. Enter ID `858224124`.<br>2. Select day `00`, month `00`, year `1994` from the dropdowns.<br>3. Do not submit yet - observe the date fields. | No inline error message. |

## Requirement 1.2 - Birth date entry (typing directly)

| ID | Title | Preconditions | Steps | Expected Result |
|---|---|---|---|---|
| 1.2.10 | Type a valid, existing date - 10.02.1994 | Common preconditions | 1. Enter ID `858224124`.<br>2. Type `10`, `02`, `1994` directly into the day/month/year fields (not via dropdown selection).<br>3. Do not submit yet - observe the date fields. | Same behavior as 1.2.1: no inline error message, fields accepted. |
| 1.2.11 | Type a year outside the dropdown's range - 1800 | Common preconditions | 1. Enter ID `858224124`.<br>2. Type day `10` and month `02`, then type `1800` into the year field.<br>3. Do not submit yet - observe the year field. | An inline error message is shown; 1800 is outside any plausible range the system should accept. |
| 1.2.12 | Type a future year - 2050 | Common preconditions | 1. Enter ID `858224124`.<br>2. Type day `10` and month `02`, then type `2050` into the year field.<br>3. Do not submit yet - observe the year field. | An inline error message is shown; a birth date cannot be in the future. |
| 1.2.13 | Type a day that doesn't exist in February - 31.2 | Common preconditions | 1. Enter ID `858224124`.<br>2. Type `31` into the day field and `02` into the month field.<br>3. Do not submit yet - observe the date fields. | An inline error message is shown, matching the expected (correct) behavior for 1.2.2 - this re-checks the same invalid combination via typing instead of dropdown selection. |
| 1.2.14 | Type a day that doesn't exist at all - 32 | Common preconditions | 1. Enter ID `858224124`.<br>2. Type `32` into the day field.<br>3. Do not submit yet - observe the day field. | An inline error message is shown; no month has 32 days. |
| 1.2.15 | Type non-numeric characters into the year field | Common preconditions | 1. Enter ID `858224124`.<br>2. Type the letters `abc` into the year field.<br>3. Do not submit yet - observe the year field. | The characters are rejected or an inline error message is shown. |
| 1.2.16 | Type non-numeric characters into the month field | Common preconditions | 1. Enter ID `858224124`.<br>2. Type the letters `abc` into the month field.<br>3. Do not submit yet - observe the month field. | The characters are rejected or an inline error message is shown. |

## Requirement 2.1 - Submission with valid, matching voter data

| ID | Title | Preconditions | Steps | Expected Result |
|---|---|---|---|---|
| 2.1.1 | Submit with real, matching ID and birth date | Common preconditions, plus: the tester's own real ID number and birth date are known (not recorded here - see privacy note above). | 1. Enter the tester's own real ID number.<br>2. Enter the tester's own real birth date.<br>3. Click "לאיתור מקום קלפי".<br>4. Observe the result. | A result screen opens showing the polling station name, address, station number, the tester's serial number at that station, and accessibility details. |
| 2.1.2 | Submit with a real, valid-format ID but a non-matching birth date | Common preconditions, plus: the tester's own real ID number is known (not recorded here). | 1. Enter the tester's own real ID number.<br>2. Enter a birth date that does **not** match that ID's registry record.<br>3. Click "לאיתור מקום קלפי".<br>4. Observe the result. | An appropriate "no matching voter found" message is shown - not the result screen from 2.1.1. |
| 2.1.3 | Submit with fictitious details matching no registered voter - 858224124, 10.02.1994 | Common preconditions | 1. Enter ID `858224124`.<br>2. Enter birth date `10.02.1994`.<br>3. Click "לאיתור מקום קלפי".<br>4. Observe the result. | An appropriate "no matching voter found" message is shown. |
| 2.1.4 | A citizen turning 18 exactly on election day (27.10.2026) | Requires the real ID number and birth date of a registered citizen whose 18th birthday is exactly 27.10.2026. **Not available to the tester as of this writing** - see `STP.md` Risks. | 1. Enter that citizen's real ID number.<br>2. Enter that citizen's real birth date.<br>3. Click "לאיתור מקום קלפי".<br>4. Observe the result. | A result screen opens as in 2.1.1 - a citizen turning 18 on election day itself is eligible to vote. |
| 2.1.5 | A citizen turning 18 the day after election day | Requires the real ID number and birth date of a registered citizen whose 18th birthday is 28.10.2026 (one day after the election). | 1. Enter that citizen's real ID number.<br>2. Enter that citizen's real birth date.<br>3. Click "לאיתור מקום קלפי".<br>4. Observe the result. | An age-ineligibility message is shown (per Requirement 2.2 below) - this citizen is still 17 on election day. |

## Requirement 2.2 - Submission for a registered citizen under voting age

| ID | Title | Preconditions | Steps | Expected Result |
|---|---|---|---|---|
| 2.2.1 | Submit with the real ID and birth date of a registered citizen under voting age | Requires the real ID number and birth date of a registered citizen well under 18. Not currently available to the tester - same constraint as 2.1.4/2.1.5. | 1. Enter that citizen's real ID number.<br>2. Enter that citizen's real birth date.<br>3. Click "לאיתור מקום קלפי".<br>4. Observe the result. | An appropriate message is shown indicating the citizen is not eligible to vote due to age - not the result screen from 2.1.1. |

## Requirement 2.3 - Rapid double-click on the submit button

| ID | Title | Preconditions | Steps | Expected Result |
|---|---|---|---|---|
| 2.3.1 | Submit with real, matching data and double-click "לאיתור מקום קלפי" | Common preconditions, plus: the tester's own real ID number and birth date are known (not recorded here). | 1. Enter the tester's own real ID number and birth date.<br>2. Click "לאיתור מקום קלפי" twice in quick succession.<br>3. Observe how many requests are sent and the button's state immediately after the first click. | Only a single request is sent; the button is locked or hidden immediately after the first click. The result screen matches 2.1.1. |

## Requirement 2.4 - Browser back button after submission

| ID | Title | Preconditions | Steps | Expected Result |
|---|---|---|---|---|
| 2.4.1 | Click the browser's back button after a successful submission | Common preconditions, plus: the tester's own real ID number and birth date are known (not recorded here); complete 2.1.1 first to reach the result screen. | 1. From the result screen (after a successful submission), click the browser's back button.<br>2. Observe the form's state. | The form returns to its normal, empty-fill state (not a broken or partially-filled state). |
