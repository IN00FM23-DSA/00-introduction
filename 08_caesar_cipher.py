"""
Exercise 7 — Caesar Cipher (Challenging)
=================================================================
Implement caesar_cipher(text, shift) that encodes a message by
shifting every letter forward by `shift` positions in the
alphabet, wrapping back to 'a'/'A' after 'z'/'Z'. There's no
built-in for this — write the loop.

Rules:
  • Only shift letters (char.isalpha()); leave spaces, digits,
    and punctuation unchanged.
  • Keep uppercase letters uppercase and lowercase letters
    lowercase.
  • For each letter:
        chr((ord(char) - base + shift) % 26 + base)
    where base is ord('A') or ord('a') depending on case.

Example:
    caesar_cipher("Hello World", 3)  →  "Khoor Zruog"
=================================================================
"""

def caesar_cipher(text: str, shift: int) -> str:
    """Return text with each letter shifted forward by shift positions."""
    # YOUR CODE HERE
    pass


if __name__ == "__main__":
    print(caesar_cipher("Hello World", 3))  # Expected: Khoor Zruog
