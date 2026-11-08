# Notification Service - Unit Tests

Unit test suite for a notification service that sends a message by SMS or
email, falls back to email when the SMS gateway is down, respects quiet hours,
writes a log file and prints the channel used.

## What is tested

- **Channel choice:** a user with a phone gets an SMS and no email; a user
  without a phone gets an email and no SMS (`assert_called_once_with` /
  `assert_not_called` on mocked clients)
- **SMS failure:** the SMS client raises `ConnectionError` (`side_effect`),
  and the message must be sent by email without an exception
- **Log file:** two notifications append two lines in the exact
  `channel|name|message` format, for both the SMS and the email channel
  (`tmp_path`)
- **Console output:** "sent via sms" / "sent via email" (`capsys`)
- **Quiet hours:** `QUIET_HOURS` set with `monkeypatch.setenv`, and the clock
  replaced with `monkeypatch.setattr`. Boundary hours on both sides of each
  edge, for a range that crosses midnight (22-7: 21, 22, 23, 0, 6, 7) and one
  that does not (13-15: 12, 13, 14, 15)

All expected results come from the specification in the module docstring,
not from the implementation.

## Techniques

Mocking external dependencies with `unittest.mock.Mock` (`side_effect`,
`assert_called_once_with`, `assert_not_called`), `monkeypatch` for environment
variables and for replacing a function where it is used
(`notifier.get_current_hour`, not `clock.get_current_hour`), `tmp_path`,
`capsys`, fixtures shared through `conftest.py`, boundary value analysis,
`parametrize` with readable ids, custom markers (`smoke`, `regression`)
registered in `pytest.ini`, and `xfail(strict=True)` on single parametrized
rows with `pytest.param(..., marks=...)`.

## Bugs found

| ID | Description | Found by |
|---|---|---|
| BUG-01 | When the SMS client raises `ConnectionError`, `notify` raises the exception instead of falling back to email (it catches `TimeoutError` instead) | `test_sms_connection_error_falls_back_to_email` |
| BUG-02 | Quiet hours that cross midnight (`"22-7"`) are never detected, so an SMS is sent at 22, 23, 0 and 6 | `test_only_email_in_quiet_hours[22-7-at-22-email]` and 3 more rows |

Tests for open bugs are marked `xfail(strict=True)`, so the suite stays green
while the bugs exist and turns red as soon as one is fixed, as a reminder to
remove the marker. For BUG-02 only the 4 failing rows are marked; the other
6 rows of the same test keep guarding the code.

## Test quality check

- The suite was run against a copy of the module with both bugs fixed: the
  5 xfail tests turned into `XPASS(strict)` failures and everything else
  passed, confirming that each failure was caused by a real bug.
- Manual mutation testing, each caught by at least one test: log opened with
  `"w"` instead of `"a"`, missing newline in the log line, log fields in the
  wrong order, log channel always "sms", email always sent, SMS sent with the
  wrong text, quiet hours assumed when `QUIET_HOURS` is not set, and two
  "fixes" for BUG-02 that break the 13-15 range.

## Run

From `03-pytest-fundamentals/`:

```
pip install -r requirements.txt
pytest notification-service -v
pytest notification-service -m smoke
```
