# 00-introduction

These are warm-up exercises. Exercises 1–5 are small, everyday problems
that Python's built-in functions solve in a single line — the goal is
to find the simplest built-in function for the job. Exercises 6–7 have
no such built-in, so write out the simple step-by-step algorithm
yourself.

## The exercises

| Exercise | File | Difficulty | Points |
|---|---|---|---|
| 1 | `01_find_largest.py` | Easy | 1 |
| 2 | `02_sort_names.py` | Easy | 1 |
| 3 | `03_even_or_odd.py` | Easy | 1 |
| 4 | `04_count_words.py` | Easy | 1 |
| 5 | `05_average_grades.py` | Easy | 1 |
| 6 | `07_fibonacci.py` | Easy | 1 |
| 7 | `08_caesar_cipher.py` | Challenging | 1 |

Each exercise file has a function with `# YOUR CODE HERE` for you to fill
in, and a matching `test_*.py` file you can use to check your work as you
go. You don't need to touch the test files — they're just there to help
you see how you're doing.

---

## Exercise 1 — Find the Largest Number `(Easy)`

Implement `find_largest(numbers)` that returns the biggest value in a list.

**Hint:** one built-in function does exactly this.

**Example:**
```
find_largest([3, 7, 2, 9, 4])  →  9
```

---

## Exercise 2 — Sort Names Alphabetically `(Easy)`

Implement `sort_names(names)` that returns a new list of strings in alphabetical order.

**Hint:** one built-in function returns a sorted copy of any list.

**Example:**
```
sort_names(["Charlie", "Alice", "Bob", "Diana"])  →  ['Alice', 'Bob', 'Charlie', 'Diana']
```

---

## Exercise 3 — Even or Odd `(Easy)`

Implement `even_or_odd(n)` that returns the string `"even"` or `"odd"`.

**Hint:** use the remainder operator `%` in a conditional expression: `n % 2 == 0` means the number is even.

**Example:**
```
even_or_odd(42)  →  "even"
even_or_odd(7)   →  "odd"
```

---

## Exercise 4 — Count Words `(Easy)`

Implement `count_words(sentence)` that returns how many words a sentence contains.

**Hint:** `str.split()` turns a sentence into a list of words; another built-in tells you how many items are in a list.

**Example:**
```
count_words("Hello world this is Python")  →  5
```

---

## Exercise 5 — Average Grade `(Easy)`

Implement `average_grades(grades)` that returns the average of a list of numbers.

**Hint:** one built-in adds up a list; another gives you its length.

**Example:**
```
average_grades([85, 92, 78, 90, 88])  →  86.6
```

---

## Exercise 6 — Fibonacci Sequence `(Easy)`

Implement `fibonacci(n)` that returns the first `n` numbers of the Fibonacci sequence, where each number is the sum of the two before it.

**Rules:**
- Start the list with `[0, 1]`.
- Keep appending `sequence[-1] + sequence[-2]` until the list has `n` elements.

**Example:**
```
fibonacci(8)  →  [0, 1, 1, 2, 3, 5, 8, 13]
```

---

## Exercise 7 — Caesar Cipher `(Challenging)`

Implement `caesar_cipher(text, shift)` that encodes a message by shifting every letter forward by `shift` positions in the alphabet, wrapping back to `'a'`/`'A'` after `'z'`/`'Z'`.

**Rules:**
- Only shift letters (`char.isalpha()`); leave spaces, digits, and punctuation unchanged.
- Keep uppercase letters uppercase and lowercase letters lowercase.
- For each letter: `chr((ord(char) - base + shift) % 26 + base)`, where `base` is `ord('A')` or `ord('a')` depending on case.

**Example:**
```
caesar_cipher("Hello World", 3)  →  "Khoor Zruog"
```

---

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
