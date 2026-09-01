# JPetStore Login Automation

Selenium automation project (Page Object Model) covering the login flow of
the public JPetStore demo site: https://petstore.octoperf.com/

## Structure

- `pages/` — Page Object classes (`BasePage`, `LoginPage`, `HomePage`)
- `scripts/login_scripts.py` — login test scenarios (valid/invalid login)
- `data/login_case.py` — test data container
- `main.py` — test runner
- `register_users.py` — setup script to register the demo users used by the
  tests. The demo site periodically wipes its registered users, so this
  script may need to be re-run occasionally — check that the login tests in
  `main.py` still pass first; if the valid-login cases start failing, re-run
  `register_users.py` to recreate the accounts

## Coverage

- Valid login (per registered demo user)
- Invalid username, valid password
- Valid username, invalid password
- Invalid username, invalid password
- Empty username and password

## Setup

This project is self-contained — its own virtual environment and
dependencies, independent of the rest of the portfolio.

1. From inside this folder, create and activate a virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
   (macOS/Linux: `source venv/bin/activate`)
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and fill in real values — either register
   your own demo users at petstore.octoperf.com (see `register_users.py`) or
   use existing ones:
   ```
   TOMER_USERNAME=...
   TOMER_PASSWORD=...
   TOMER2_USERNAME=...
   TOMER2_PASSWORD=...
   ```
4. Run:
   ```
   python main.py
   ```

## Evidence

TODO: run the suite and save a console output / screenshot of a full passing
run into `evidence/`.

## Future improvements

- Convert the runner from a hand-rolled script (prints + try/except) to
  pytest, for real test discovery, fixtures, and standard reporting.
