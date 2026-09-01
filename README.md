# QA Portfolio — Tomer Levin

Manual QA testing portfolio, built to demonstrate practical, industry-standard
testing skills for an entry-level QA role.

Each project in this repo covers a real, publicly available system and
applies a structured testing process — manual or automated. Deliverables
vary by project — see each project's own README for its specific artifacts
(test plan, test cases, bug reports, automation suite, etc.).

## About Me

ISTQB Certified Tester – Foundation Level (CTFL). Building this portfolio
while searching for a first QA role, to demonstrate hands-on manual testing
skills on real, publicly available systems.

## Projects

| # | Project | Description | System Under Test | Status |
|---|---------|--------------|--------------------|--------|
| 01 | [Voting Station Locator](01-voting-station-locator/) | Full manual test cycle on a government voting-station lookup tool | [gov.il — Voting Station Locator](https://www.gov.il/apps/moin/bocharim/) | In progress |
| 02 | [JPetStore Login Automation](02-jpetstore-login-automation/) | Selenium (POM) automation suite for a login flow | [JPetStore demo](https://petstore.octoperf.com/) | In progress |

## Environment setup (for Python-based projects)

Python-based projects in this repo (e.g. project 02) share a single virtual
environment and `requirements.txt` at the repo root:

```
python -m venv venv
.\venv\Scripts\Activate.ps1   # PowerShell; on macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
```

Activate this environment before running any Python project's scripts. Each
project may still have its own `.env` for project-specific secrets — see
that project's README.

## Skills demonstrated

Aggregated across all projects in this portfolio — updated as new projects are added.

- Manual functional testing
- Test planning (ISTQB / IEEE 829 style)
- Test case design (positive, negative, boundary)
- Exploratory testing
- Bug reporting
- Usability & basic accessibility checks
- Cross-browser / responsive checks
- Clear technical documentation
- Test automation (Selenium, Page Object Model)

## Contact

- 📧 tomer9tomer@gmail.com
- 💼 [LinkedIn](https://www.linkedin.com/in/tomer-levin-970874336/)
