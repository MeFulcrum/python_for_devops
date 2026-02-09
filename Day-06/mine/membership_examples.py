"""Membership operators examples (Day-06 notes)

Demonstrates `in` and `not in` with lists, sets and strings. Uses examples for clarity.
Run: python membership_examples.py
"""

from __future__ import annotations


def main() -> None:
    print("Membership operators demo")

    seq = [1, 2, 3]
    print(f"2 in {seq} -> {2 in seq}")
    print(f"5 in {seq} -> {5 in seq}")

    s = {"apple", "banana"}
    print(f"'banana' in {s} -> {'banana' in s}")

    txt = "hello"
    print(f"'h' in '{txt}' -> {'h' in txt}")
    print(f"'z' not in '{txt}' -> {'z' not in txt}")


if __name__ == '__main__':
    main()
