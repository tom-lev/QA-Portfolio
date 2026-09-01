# JPetStore Login Automation

Selenium automation project (Page Object Model) covering the login flow of
the public JPetStore demo site: https://petstore.octoperf.com/

## Structure

- `pages/` — Page Object classes (`BasePage`, `LoginPage`, `HomePage`)
- `scripts/login_scripts.py` — login test scenarios (valid/invalid login)
- `data/login_case.py` — test data container
- `main.py` — test runner
- `register_users.py` — one-time setup script to register the demo users
  used by the tests

## Coverage

- Valid login (per registered demo user)
- Invalid username, valid password
- Valid username, invalid password
- Invalid username, invalid password
- Empty username and password

## Setup

1. `pip install -r requirements.txt`
2. Copy `.env.example` to `.env` and fill in real values — either register
   your own demo users at petstore.octoperf.com (see `register_users.py`) or
   use existing ones:
   ```
   TOMER_USERNAME=...
   TOMER_PASSWORD=...
   TOMER2_USERNAME=...
   TOMER2_PASSWORD=...
   ```
3. Run:
   ```
   python main.py
   ```

## Evidence

TODO: run the suite and save a console output / screenshot of a full passing
run into `evidence/`.

## Future improvements

- Convert the runner from a hand-rolled script (prints + try/except) to
  pytest, for real test discovery, fixtures, and standard reporting.
