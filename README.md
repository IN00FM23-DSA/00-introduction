# 00 — Introduction

Warm-up exercises for the Data Structures & Algorithms course. See [`00_introduction.md`](00_introduction.md) for the exercise descriptions.

## Structure

- `NN_name.py` — one stub per exercise. Implement the function where it says `# YOUR CODE HERE`.
- `test_NN_name.py` — the pytest tests for that exercise.
- `_helpers.py` — shared helper the test files use to load the numbered exercise modules.

## Running the tests

```bash
pip install -r requirements.txt
pytest -v
```

Tests also run automatically on every push and pull request via GitHub Actions (see `.github/workflows/tests.yml`).
