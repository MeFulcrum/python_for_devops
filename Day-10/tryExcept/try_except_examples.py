"""try_except_examples.py
Interactive examples showing common Python exceptions and how to handle them.
Run with: python try_except_examples.py

Each example prints a suggested sample input.
"""

def example_index_error():
    print("\nExample: IndexError")
    print("Sample input: list: a b c   index: 10")
    try:
        items = input("Enter items separated by spaces: ").split()
        idx = int(input("Enter index to access: "))
        print(f"Item at {idx}: {items[idx]}")
    except IndexError as e:
        print(f"Caught IndexError: {e}")


def example_value_error():
    print("\nExample: ValueError")
    print("Sample input: not-an-int")
    try:
        s = input("Enter an integer: ")
        val = int(s)  # ValueError if s is not an integer representation
        print(f"You entered integer {val}")
    except ValueError as e:
        print(f"Caught ValueError: {e}")


def example_type_error():
    print("\nExample: TypeError")
    print("Sample input: number: 5   text: hello")
    try:
        n = int(input("Enter a number: "))
        text = input("Enter some text: ")
        # This will raise TypeError: unsupported operand type(s) for +: 'int' and 'str'
        result = n + text
        print("Result:", result)
    except TypeError as e:
        print(f"Caught TypeError: {e}")


def example_key_error():
    print("\nExample: KeyError")
    print("Sample input: {'a':1}   key: b")
    try:
        d = {k: int(v) for k, v in (pair.split(':') for pair in input("Enter key:value pairs (comma separated), e.g. a:1,b:2: ").split(','))}
        key = input("Enter key to lookup: ")
        print(f"Value for '{key}': {d[key]}")
    except KeyError as e:
        print(f"Caught KeyError: {e}")
    except Exception as e:
        print(f"Input parsing error: {e}")


def example_file_not_found_error():
    print("\nExample: FileNotFoundError")
    print("Sample input: filename that does not exist")
    try:
        fname = input("Enter filename to open: ")
        with open(fname, 'r') as f:
            print(f"First line: {f.readline()}")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")


def example_zero_division_error():
    print("\nExample: ZeroDivisionError")
    print("Sample input: 0")
    try:
        denom = int(input("Enter denominator for 10 / denom: "))
        print(10 / denom)
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    except ValueError as e:
        print(f"Bad number: {e}")


def example_import_error():
    print("\nExample: ImportError / ModuleNotFoundError")
    print("Sample input: some_nonexistent_module")
    try:
        modname = input("Enter module name to import: ")
        __import__(modname)
        print(f"Imported {modname} successfully")
    except ModuleNotFoundError as e:
        print(f"Caught ModuleNotFoundError: {e}")
    except ImportError as e:
        print(f"Caught ImportError: {e}")


def example_attribute_error():
    print("\nExample: AttributeError")
    print("Sample input: call .upper() on a number")
    try:
        obj = input("Enter a value (try a number like 5): ")
        # try to call string method on the raw input converted to int
        maybe_num = int(obj)
        print(maybe_num.upper())  # int has no attribute 'upper' -> AttributeError
    except AttributeError as e:
        print(f"Caught AttributeError: {e}")
    except ValueError:
        print("Value not an int; trying string .upper() instead:")
        s = obj
        print(s.upper())


def example_recursion_error():
    print("\nExample: RecursionError")
    print("This will trigger a RecursionError automatically")
    try:
        def recurse():
            return recurse()
        recurse()
    except RecursionError as e:
        print(f"Caught RecursionError: {e}")


def main():
    examples = [
        ("IndexError", example_index_error),
        ("ValueError", example_value_error),
        ("TypeError", example_type_error),
        ("KeyError", example_key_error),
        ("FileNotFoundError", example_file_not_found_error),
        ("ZeroDivisionError", example_zero_division_error),
        ("ImportError", example_import_error),
        ("AttributeError", example_attribute_error),
        ("RecursionError", example_recursion_error),
    ]

    print("Try/Except examples. Press Ctrl+C to exit at any prompt.")
    try:
        for name, func in examples:
            print("\n---", name, "example ---")
            func()
            cont = input("Press Enter to continue to next example, or type 'q' to quit: ")
            if cont.lower() == 'q':
                break
    except KeyboardInterrupt:
        print("\nInterrupted by user (KeyboardInterrupt)")

if __name__ == '__main__':
    main()
