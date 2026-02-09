"""Logical operators examples (Day-06 notes)

Demonstrates and, or, not and short-circuit behavior. Uses simple functions to show evaluation.
Run: python logical_examples.py
"""

from __future__ import annotations


def truthy(name: str, value: bool) -> bool:
    print(f"evaluating {name} -> {value}")
    return value


def main() -> None:
    print("Logical operators demo")

    print("-- Simple boolean ops --")
    a = True
    b = False
    print(f"a and b -> {a and b}")
    print(f"a or b -> {a or b}")
    print(f"not a -> {not a}")

    print("\n-- Short-circuit demonstration --")
    print("Case: False and truthy('A', True)")
    print(False and truthy('A', True))
    print("Case: True or truthy('B', False)")
    print(True or truthy('B', False))


if __name__ == '__main__':
    main()
