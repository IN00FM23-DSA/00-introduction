# 00-introduction

Welcome! This topic has one or more small Python exercises to work through.
See [`00_introduction.md`](00_introduction.md) for the full exercise
descriptions.

## The exercises

| Exercise | File | Points |
|---|---|---|
| 1 | `01_find_largest.py` | 2 |
| 2 | `02_sort_names.py` | 2 |
| 3 | `03_even_or_odd.py` | 1 |
| 4 | `04_count_words.py` | 2 |
| 5 | `05_average_grades.py` | 2 |
| 6 | `07_fibonacci.py` | 2 |
| 7 | `08_caesar_cipher.py` | 3 |

Each exercise file has a function with `# YOUR CODE HERE` for you to fill
in, and a matching `test_*.py` file you can use to check your work as you
go. You don't need to touch the test files — they're just there to help
you see how you're doing.

## Step by step

1. **Clone this repo**:
   ```
   git clone <this repo's URL>
   cd <the folder that creates>
   ```
2. **Set up a virtual environment and install dependencies**:
   ```
   python -m venv .venv
   .venv\Scripts\activate      # Windows — use "source .venv/bin/activate" on macOS/Linux
   pip install -r requirements.txt
   ```
3. **Open the folder in VS Code**: `code .` (or File → Open Folder). If
   prompted "This workspace has extension recommendations", click
   **Install** — this adds a beaker-shaped **Testing** icon to the left
   sidebar.
4. **Run the tests before changing anything**, just to see where you're
   starting from. Click the beaker icon, then the play button at the top
   of the Test Explorer panel — everything will be red at first, and
   that's completely normal.
5. **Implement each exercise** in its source file, one at a time.
6. **Re-run the tests** after each change to see your progress. Prefer a
   terminal? `pytest -v` does the same check for all exercises at once.
7. **Work locally** until all assignment tests pass.
8. **Push your work back** to the GitHub organization when you're ready:
   ```
   git add -A
   git commit -m "Exercises done"
   git push
   ```
   A quick check runs automatically on GitHub afterward — you can peek at
   it under this repo's **Actions** tab if you're curious, but it's just
   extra feedback, nothing you need to act on.
9. **Assignment completed — good job!**
