"""demo_exceptions.py
Automated demonstration of exception handling.
Shows each exception type with a real example that triggers it.
Run with: python demo_exceptions.py
"""

print("=" * 70)
print("PYTHON EXCEPTION HANDLING DEMO")
print("=" * 70)

# 1. IndexError
print("\n[1] IndexError - Accessing list index that doesn't exist")
print("-" * 70)
try:
    items = ['apple', 'banana', 'cherry']
    print(f"List: {items}")
    print(f"Attempting to access index 10...")
    print(items[10])
except IndexError as e:
    print(f"✓ CAUGHT IndexError: {e}")

# 2. ValueError
print("\n[2] ValueError - Converting incompatible string to number")
print("-" * 70)
try:
    s = "not-a-number"
    print(f"Input string: '{s}'")
    print(f"Attempting int('{s}')...")
    val = int(s)
except ValueError as e:
    print(f"✓ CAUGHT ValueError: {e}")

# 3. TypeError
print("\n[3] TypeError - Incompatible types in operation")
print("-" * 70)
try:
    n = 5
    text = "hello"
    print(f"Number: {n}, Text: '{text}'")
    print(f"Attempting: {n} + '{text}'...")
    result = n + text
except TypeError as e:
    print(f"✓ CAUGHT TypeError: {e}")

# 4. KeyError
print("\n[4] KeyError - Accessing non-existent dictionary key")
print("-" * 70)
try:
    person = {'name': 'Alice', 'age': 30}
    print(f"Dictionary: {person}")
    print("Attempting to access person['email']...")
    email = person['email']
except KeyError as e:
    print(f"✓ CAUGHT KeyError: {e}")

# 5. FileNotFoundError
print("\n[5] FileNotFoundError - File does not exist")
print("-" * 70)
try:
    print("Attempting to open 'nonexistent_file.txt'...")
    with open('nonexistent_file.txt', 'r') as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"✓ CAUGHT FileNotFoundError: {e}")

# 6. ZeroDivisionError
print("\n[6] ZeroDivisionError - Division by zero")
print("-" * 70)
try:
    print("Attempting: 10 / 0...")
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"✓ CAUGHT ZeroDivisionError: {e}")

# 7. ModuleNotFoundError
print("\n[7] ModuleNotFoundError - Importing non-existent module")
print("-" * 70)
try:
    print("Attempting: import nonexistent_module...")
    __import__('nonexistent_module')
except ModuleNotFoundError as e:
    print(f"✓ CAUGHT ModuleNotFoundError: {e}")

# 8. AttributeError
print("\n[8] AttributeError - Object has no attribute")
print("-" * 70)
try:
    num = 42
    print(f"Number: {num}")
    print("Attempting: num.upper() [strings have .upper(), not integers]...")
    num.upper()
except AttributeError as e:
    print(f"✓ CAUGHT AttributeError: {e}")

# 9. NameError
print("\n[9] NameError - Using undefined variable")
print("-" * 70)
try:
    print("Attempting to use variable that was never defined...")
    print(undefined_var)
except NameError as e:
    print(f"✓ CAUGHT NameError: {e}")

# 10. RecursionError
print("\n[10] RecursionError - Maximum recursion depth exceeded")
print("-" * 70)
try:
    print("Attempting infinite recursion...")
    def infinite_loop():
        return infinite_loop()
    infinite_loop()
except RecursionError as e:
    print(f"✓ CAUGHT RecursionError: {e}")

# 11. TypeError with wrong number of arguments
print("\n[11] TypeError - Wrong number of function arguments")
print("-" * 70)
try:
    def greet(name, age):
        return f"{name} is {age} years old"
    print("Function: greet(name, age)")
    print("Attempting: greet('Alice')  [missing 'age' argument]...")
    result = greet('Alice')
except TypeError as e:
    print(f"✓ CAUGHT TypeError: {e}")

# 12. Multiple exception handling
print("\n[12] Multiple exception handling in one block")
print("-" * 70)
user_inputs = ['42', 'not-a-number', '100']
for idx, inp in enumerate(user_inputs):
    try:
        print(f"\nAttempt {idx + 1}: Converting '{inp}' to integer...")
        num = int(inp)
        print(f"Success! Converted to: {num}")
    except ValueError:
        print(f"✗ ValueError: '{inp}' cannot be converted to int")
    except Exception as e:
        print(f"✗ Other error: {e}")

print("\n" + "=" * 70)
print("END OF DEMO")
print("=" * 70)
