"""Bitwise operators examples (based on `Bitwise Operators.md`).

Shows: &, |, ^, ~, <<, >> with binary and decimal output for clarity.
Run:
    python bitwise_examples.py
"""

from __future__ import annotations


def illustrate(op_name: str, expr_desc: str, value:int, result:int) -> None:
    print(f"{op_name}: {expr_desc}")
    print(f"  -> {value} ({bin(value)}) => {result} ({bin(result)})\n")


def demonstrate_and() -> None:
    a, b = 5, 3  # 0b0101 & 0b0011 -> 0b0001
    print("[AND (&)]")
    print(f"a = {a} ({bin(a)})")
    print(f"b = {b} ({bin(b)})")
    print(f"a & b = {a & b} ({bin(a & b)})\n")


def demonstrate_or() -> None:
    x, y = 10, 7  # 0b1010 | 0b0111 -> 0b1111
    print("[OR (|)]")
    print(f"x = {x} ({bin(x)})")
    print(f"y = {y} ({bin(y)})")
    print(f"x | y = {x | y} ({bin(x | y)})\n")


def demonstrate_xor() -> None:
    a, b = 5, 3  # 0b0101 ^ 0b0011 -> 0b0110
    print("[XOR (^)]")
    print(f"a = {a} ({bin(a)})")
    print(f"b = {b} ({bin(b)})")
    print(f"a ^ b = {a ^ b} ({bin(a ^ b)})\n")


def demonstrate_not() -> None:
    a = 5  # ~a flips all bits; ~5 == -6 in Python (two's complement)
    print("[NOT (~)]")
    print(f"a = {a} ({bin(a)})")
    print(f"~a = {~a} ({bin(~a)})")
    # Show a common way to view bitwise NOT within an 8-bit mask
    print(f"(~a) & 0xff = { (~a) & 0xff } ({bin((~a) & 0xff)})  # 8-bit view\n")


def demonstrate_shifts() -> None:
    val = 3
    print("[Shifts (<<, >>)]")
    print(f"val = {val} ({bin(val)})")
    print(f"val << 2 = {val << 2} ({bin(val << 2)})  # left shift (multiply by 2**2)")
    val2 = 16
    print(f"{val2} ({bin(val2)}) >> 2 = {val2 >> 2} ({bin(val2 >> 2)})  # right shift (floor div by 2**2)\n")


def main() -> None:
    print("Bitwise operators demo\n" + "="*30 + "\n")
    demonstrate_and()
    demonstrate_or()
    demonstrate_xor()
    demonstrate_not()
    demonstrate_shifts()


if __name__ == '__main__':
    main()
