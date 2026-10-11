# pytest Fundamentals

Unit testing projects written with pytest while learning test automation.
Each project tests a small module against its specification, documents the
bugs found, and runs in CI on every push.

The code under test was provided as a training exercise with planted bugs.
The test design, bug analysis and documentation are my own; the final test
code was refactored for readability with AI-assisted review.

## Projects

| Project | Focus | Bugs found |
|---|---|---|
| [Registration Form](registration-form/) | Boundary values, negative tests, `pytest.raises`, `pytest.approx` | 2 |

## Run all tests

```
pip install -r requirements.txt
pytest -v
```

Requires Python 3.10+. Settings are in `pytest.ini` (`--strict-markers`,
strict xfail).
