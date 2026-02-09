"""Identity operators examples (Day-06 notes)

Demonstrates `is` and `is not` with ints and lists; uses a=10, b=5 where meaningful.
Run: python identity_examples.py
"""

from __future__ import annotations


def main() -> None:
    print("Identity operators demo")

    # Small integer caching: -5..256 are typically cached
    a = 256
    b = 256
    print(f"a=256; b=256; a is b -> {a is b}  (cached small int)")

    a = 1000
    b = 1000
    print(f"a=1000; b=1000; a is b -> {a is b}  (may be False)")

    # Lists - identity vs equality
    x = [1, 2, 3]
    y = x
    z = [1, 2, 3]
    print(f"x = {x}; y = x; z = [1,2,3]")
    print(f"x is y -> {x is y}  (same object)")
    print(f"x == z -> {x == z}  (value equality)")
    print(f"x is z -> {x is  z}  (different objects)") # False Because z is a new list
    print(f"x is not z -> {x is not z}  (different objects)")
    

if __name__ == '__main__':
    main()
