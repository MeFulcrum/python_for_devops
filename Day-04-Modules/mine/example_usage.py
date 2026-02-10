"""Example script showing how to use `my_package` (see Day-04 README)

Run:
    python example_usage.py
"""

from my_package import greet, square


def main() -> None:
    name = "Alice"
    print(greet(name))
    print(f"5 squared is {square(5)}")


if __name__ == "__main__":
    main()
