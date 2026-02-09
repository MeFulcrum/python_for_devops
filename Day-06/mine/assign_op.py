"""Assignment operators examples for Day-06

Each demonstration resets a=10 and b=5 so examples are independent and repeatable.
"""

from __future__ import annotations

def demonstrate_addition_assignment() -> None:
    """Demonstrate `a += b` starting with a=10, b=5."""
    a = 10
    b = 5
    print(f"[add] initial: a={a}, b={b}")
    a += b
    print(f"[add] after a += b -> a={a}\n")


def demonstrate_subtraction_assignment() -> None:
    """Demonstrate `a -= b` starting with a=10, b=5."""
    a = 10
    b = 5
    print(f"[sub] initial: a={a}, b={b}")
    a -= b
    print(f"[sub] after a -= b -> a={a}\n")


def demonstrate_multiplication_assignment() -> None:
    """Demonstrate `a *= b` starting with a=10, b=5."""
    a = 10
    b = 5
    print(f"[mul] initial: a={a}, b={b}")
    a *= b
    print(f"[mul] after a *= b -> a={a}\n")


def demonstrate_true_division_assignment() -> None:
    """Demonstrate `a /= b` starting with a=10, b=5."""
    a = 10
    b = 5
    print(f"[div] initial: a={a}, b={b}")
    a /= b
    print(f"[div] after a /= b -> a={a} (float)\n")


def demonstrate_floor_division_assignment() -> None:
    """Demonstrate `a //= b` starting with a=10, b=5."""
    a = 10
    b = 5
    print(f"[floordiv] initial: a={a}, b={b}")
    a //= b
    print(f"[floordiv] after a //= b -> a={a}\n")


def demonstrate_modulo_assignment() -> None:
    """Demonstrate `a %= b` starting with a=10, b=5."""
    a = 10
    b = 5
    print(f"[mod] initial: a={a}, b={b}")
    a %= b
    print(f"[mod] after a %= b -> a={a}\n")


def demonstrate_power_assignment() -> None:
    """Demonstrate `a **= b` starting with a=10, b=5."""
    a = 10
    b = 5
    print(f"[pow] initial: a={a}, b={b}")
    a **= b
    print(f"[pow] after a **= b -> a={a}\n")


def main() -> None:
    demonstrate_addition_assignment()
    demonstrate_subtraction_assignment()
    demonstrate_multiplication_assignment()
    demonstrate_true_division_assignment()
    demonstrate_floor_division_assignment()
    demonstrate_modulo_assignment()
    demonstrate_power_assignment()


if __name__ == '__main__':
    main()
