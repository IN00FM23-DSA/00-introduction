# Topic 0: Introduction

These are warm-up exercises. Exercises 1–5 are small, everyday problems that Python's built-in functions solve in a single line — the goal is to find the simplest built-in function for the job. Exercises 6–7 have no such built-in, so write out the simple step-by-step algorithm yourself.

| Exercise | Difficulty | Function |
|---|---|---|
| 1 | Easy | `find_largest` |
| 2 | Easy | `sort_names` |
| 3 | Easy | `even_or_odd` |
| 4 | Easy | `count_words` |
| 5 | Easy | `average_grades` |
| 6 | Easy | `fibonacci` |
| 7 | Challenging | `caesar_cipher` |

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
