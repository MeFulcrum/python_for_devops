"""Operator precedence examples (Day-06 notes)

Shows how parentheses affect evaluation and demonstrates precedence with arithmetic and logical expressions.
Run: python precedence_examples.py
"""

from __future__ import annotations


def main() -> None:
    print("Precedence operators demo")
    expr1 = 2 + 3 * 4
    expr2 = (2 + 3) * 4
    print(f"2 + 3 * 4 = {expr1}  # multiplication before addition")
    print(f"(2 + 3) * 4 = {expr2}  # parentheses change order")

    # Logical precedence: not > and > or
    a, b, c = False, True, False
    print(f"not a and b or c -> {not a and b or c}  # evaluated as ((not a) and b) or c")


if __name__ == '__main__':
    main()
