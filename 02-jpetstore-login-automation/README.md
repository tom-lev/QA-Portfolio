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

This project uses the shared virtual environment and `requirements.txt` at
the repo root (`QA-Portfolio/venv`, `QA-Portfolio/requirements.txt`) — see
the root README for setup. Once the environment is active:

1. Copy `.env.example` to `.env` (inside this folder) and fill in real
   values — either register your own demo users at petstore.octoperf.com
   (see `register_users.py`) or use existing ones:
   ```
   TOMER_USERNAME=...
   TOMER_PASSWORD=...
   TOMER2_USERNAME=...
   TOMER2_PASSWORD=...
   ```
2. Run (from inside this folder):
   ```
   python main.py
   ```

## Evidence

TODO: run the suite and save a console output / screenshot of a full passing
run into `evidence/`.

## Future improvements

- Convert the runner from a hand-rolled script (prints + try/except) to
  pytest, for real test discovery, fixtures, and standard reporting.
