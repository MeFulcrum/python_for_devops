"""
UNDERSTANDING repr() - Representation Function

What does repr() do?
- repr() returns a STRING that represents the actual value
- It shows you what the value ACTUALLY IS, including special characters
- It shows quotes around strings so you can see where they start/end
- It converts escape sequences to their literal forms (\\n instead of newline)

Why use repr()?
- To see the "true" value of something, not just how it displays
- To debug and understand what your code is actually storing
- To see hidden characters like newlines, tabs, etc.
"""

print("=" * 70)
print("EXAMPLE 1: Simple String with Newline")
print("=" * 70)

my_string = "hello\nworld"

print("\nUsing print():")
print("  print(my_string)")
print("  Output:")
print(my_string)
print("  ^ Notice: The string appears on TWO lines!")

print("\nUsing repr():")
print("  repr(my_string)")
print("  Output:")
print(repr(my_string))
print("  ^ Notice: We see the ACTUAL string with \\n shown literally!")

print("\n  Comparison:")
print("    print():  Shows how the string LOOKS when displayed")
print("    repr():   Shows what the string ACTUALLY IS")


print("\n" + "=" * 70)
print("EXAMPLE 2: String with Tab Character")
print("=" * 70)

my_string = "Name\tAge\tCity"

print("\nUsing print():")
print("  print(my_string)")
print("  Output:")
print(my_string)
print("  ^ The tab creates spacing")

print("\nUsing repr():")
print("  repr(my_string)")
print("  Output:")
print(repr(my_string))
print("  ^ We see \\t (the actual tab character representation)")


print("\n" + "=" * 70)
print("EXAMPLE 3: Raw String vs Normal String")
print("=" * 70)

normal = "hello\nworld"
raw = r"hello\nworld"

print("\nNormal string (WITHOUT r):")
print("  print():")
print(normal)
print("  repr():")
print(repr(normal))

print("\nRaw string (WITH r):")
print("  print():")
print(raw)
print("  repr():")
print(repr(raw))

print("\n  Key difference:")
print("    Normal: 'hello\\nworld'   <- Two actual lines")
print("    Raw:    'hello\\\\nworld' <- One line with literal backslash-n")


print("\n" + "=" * 70)
print("EXAMPLE 4: In the r_string_simple.py File")
print("=" * 70)

string_with_r = r"hello\nworld"

print("\nThe line in that file was:")
print("  print(f\"  Actual value: {repr(string_with_r)}\")")

print("\nBreakdown:")
print("  string_with_r = r\"hello\\nworld\"")
print("  repr(string_with_r) converts it to:", repr(string_with_r))
print("  So it prints:", f"  Actual value: {repr(string_with_r)}")

print("\n  Why use repr() there?")
print("  -> To show the USER what the string actually contains")
print("  -> To make it clear that \\n is LITERAL, not a newline")


print("\n" + "=" * 70)
print("EXAMPLE 5: Different Types")
print("=" * 70)

examples = [
    ("String", "hello"),
    ("String with newline", "hello\nworld"),
    ("String with quote", 'He said "Hi"'),
    ("Integer", 42),
    ("Float", 3.14),
    ("List", [1, 2, 3]),
    ("None", None),
]

print("\nValue              | print()          | repr()")
print("-" * 70)

for name, value in examples:
    print(f"{name:20} | {str(value)[:15]:15} | {repr(value)}")


print("\n" + "=" * 70)
print("SUMMARY: When to use repr()")
print("=" * 70)

print("\nUse print() when:")
print("  - You want to see how something DISPLAYS to the user")
print("  - You want clean, readable output")
print("  Example: print(my_name)  # Shows: John")

print("\nUse repr() when:")
print("  - You want to see what something ACTUALLY IS")
print("  - You're DEBUGGING and need to see hidden characters")
print("  - You want to see string quotes and escape sequences")
print("  Example: print(repr(my_name))  # Shows: 'John'")

print("\nCommon pattern (like in r_string_simple.py):")
print("  print(f\"Value: {repr(my_var)}\")")
print("  This shows both:")
print("    - Label + context (from the f-string)")
print("    - Actual stored value (from repr())")
