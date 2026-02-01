"""CLI args examples for Day-05

Demonstrates two approaches:
 - Using argparse for robust CLI parsing
 - Inspecting raw sys.argv for simple scripts

Run examples:
  python cli_args.py --name Alice -c 2 --verbose extra1 extra2
  python cli_args.py foo bar
"""

from __future__ import annotations
import argparse
import sys


def using_argparse(argv: list[str] | None = None) -> None:
    """Demonstrate argparse usage."""
    parser = argparse.ArgumentParser(description="Demo: command-line arguments with argparse")
    parser.add_argument('-n', '--name', type=str, default='World', help='Name to greet')
    parser.add_argument('-c', '--count', type=int, default=1, help='Number of times to greet')
    parser.add_argument('--verbose', action='store_true', help='Verbose output')
    parser.add_argument('extras', nargs='*', help='Extra positional arguments')

    args = parser.parse_args(argv)

    for i in range(args.count):
        greeting = f"Hello, {args.name}!"
        if args.verbose:
            print(f"[{i+1}/{args.count}] greeting='{greeting}', extras={args.extras}")
        else:
            print(greeting)


def using_sys_argv() -> None:
    """Quick demo of reading raw argv values from sys.argv."""
    # sys.argv[0] is the script name
    if len(sys.argv) <= 1:
        print("No positional args provided. Example: python cli_args.py foo bar")
        return
    print("Raw argv (excluding script name):", sys.argv[1:])


def main() -> None:
    # When invoked normally we use argparse
    using_argparse()


if __name__ == '__main__':
    main()
