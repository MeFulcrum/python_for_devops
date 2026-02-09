"""Arithmetic operators examples (Day-06 notes)

Demonstrates basic arithmetic operations with a=10 and b=5.
Run: python arithmetic_examples.py
"""

from __future__ import annotations


def main() -> None:
    a = 10
    b = 5
    print("Arithmetic operators demo (a=10, b=5)")
    print(f"a + b = {a + b}")
    print(f"a - b = {a - b}")
    print(f"a * b = {a * b}")
    print(f"a / b = {a / b}  (float division)")
    print(f"a // b = {a // b}  (floor division)")
    print(f"a % b = {a % b}  (modulo)")
    print(f"a ** b = {a ** b}  (power)")


if __name__ == '__main__':
    main()
