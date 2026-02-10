"""
UNDERSTANDING THE 'r' PREFIX IN PYTHON STRINGS

Simple Explanation:
- WITHOUT 'r':  Backslash (\) is treated as a SPECIAL CHARACTER (escape character)
- WITH 'r':     Backslash (\) is treated as a NORMAL CHARACTER (literal)

Let's see examples side-by-side.
"""

print("=" * 70)
print("EXAMPLE 1: The Newline Character \\n")
print("=" * 70)

# WITHOUT r: \n is interpreted as NEWLINE (moves to next line)
string_without_r = "hello\nworld"
print("\nWithout r prefix:")
print("  Code: \"hello\\nworld\"")
print("  Result:")
print(string_without_r)
print(f"  Actual value: {repr(string_without_r)}")

# WITH r: \n stays as LITERAL (backslash followed by n)
string_with_r = r"hello\nworld"
print("\nWith r prefix:")
print("  Code: r\"hello\\nworld\"")
print("  Result:")
print(string_with_r)
print(f"  Actual value: {repr(string_with_r)}")


print("\n" + "=" * 70)
print("EXAMPLE 2: The Tab Character \\t")
print("=" * 70)

# WITHOUT r: \t is interpreted as TAB (horizontal spacing)
string_without_r = "Name\tAge\tCity"
print("\nWithout r prefix:")
print("  Code: \"Name\\tAge\\tCity\"")
print("  Result:")
print(string_without_r)
print(f"  Actual value: {repr(string_without_r)}")

# WITH r: \t stays as LITERAL (backslash followed by t)
string_with_r = r"Name\tAge\tCity"
print("\nWith r prefix:")
print("  Code: r\"Name\\tAge\\tCity\"")
print("  Result:")
print(string_with_r)
print(f"  Actual value: {repr(string_with_r)}")


print("\n" + "=" * 70)
print("EXAMPLE 3: Windows File Path")
print("=" * 70)

# WITHOUT r: backslashes cause problems because \U, \n, \t etc. are special
# Let's use a different example without \U problem
string_without_r = "C:\\Users\\Documents"  # Need to double the backslashes!
print("\nWithout r prefix:")
print("  Code: \"C:\\\\Users\\\\Documents\"  (need double backslashes!)")
print("  Result:")
print(string_without_r)
print(f"  Actual value: {repr(string_without_r)}")
print("  Problem: We have to write \\\\ instead of just \\  (confusing!)")

# WITH r: all backslashes stay literal - perfect for Windows paths!
string_with_r = r"C:\Users\nate\Documents"
print("\nWith r prefix:")
print("  Code: r\"C:\\Users\\nate\\Documents\"")
print("  Result:")
print(string_with_r)
print(f"  Actual value: {repr(string_with_r)}")
print("  Good: Backslashes are kept as-is!")


print("\n" + "=" * 70)
print("EXAMPLE 4: Regular Expression Patterns (THE MAIN REASON!)")
print("=" * 70)

import re

# WITHOUT r: You need to escape the backslash to get what regex needs
pattern_without_r = "\\d+"  # Had to write \\ to get \d for regex
print("\nWithout r prefix:")
print("  Code: \"\\\\d+\"  (notice the double backslash!)")
print(f"  Actual pattern: {repr(pattern_without_r)}")
text = "I have 42 apples and 5 oranges"
matches = re.findall(pattern_without_r, text)
print(f"  Pattern finds numbers: {matches}")

# WITH r: Much cleaner! Write the pattern naturally
pattern_with_r = r"\d+"  # Just write \d directly - r prefix keeps it literal
print("\nWith r prefix:")
print("  Code: r\"\\d+\"  (just one backslash!)")
print(f"  Actual pattern: {repr(pattern_with_r)}")
matches = re.findall(pattern_with_r, text)
print(f"  Pattern finds numbers: {matches}")

print("\n  COMPARISON:")
print("    Without r: Need to write \"\\\\d+\"  (confusing, extra backslash)")
print("    With r:    Need to write r\"\\d+\" (clear, easy to read)")


print("\n" + "=" * 70)
print("EXAMPLE 5: Your 'brown:' Pattern")
print("=" * 70)

# WITHOUT r: "brown:" has no backslashes, so no problem
pattern_without_r = "brown:"
print("\nWithout r prefix:")
print("  Code: \"brown:\"")
print(f"  Pattern: {repr(pattern_without_r)}")
text = "The color brown: is nice"
matches = re.findall(pattern_without_r, text)
print(f"  Matches: {matches}")

# WITH r: "brown:" still works (no backslashes to escape anyway)
pattern_with_r = r"brown:"
print("\nWith r prefix:")
print("  Code: r\"brown:\"")
print(f"  Pattern: {repr(pattern_with_r)}")
matches = re.findall(pattern_with_r, text)
print(f"  Matches: {matches}")

print("\n  Note: For 'brown:' it doesn't matter because there are no backslashes.")
print("  But for regex patterns with \\d, \\w, \\s, etc., ALWAYS use r!")


print("\n" + "=" * 70)
print("SUMMARY TABLE")
print("=" * 70)

print("\nString Content        | Without r         | With r")
print("-" * 60)
print("hello\\nworld         | hello             | hello\\nworld")
print("                      | world             |")
print("-" * 60)
print("Name\\tAge            | Name    Age        | Name\\tAge")
print("-" * 60)
print("C:\\Users\\abc        | (broken/confused) | C:\\Users\\abc")
print("-" * 60)
print("\\d+ (regex)           | \\\\d+ (confusing) | \\d+ (clean!)")


print("\n" + "=" * 70)
print("GOLDEN RULE FOR REGEX")
print("=" * 70)
print("\n  ALWAYS USE r PREFIX FOR REGEX PATTERNS!")
print("  Example: pattern = r\"\\d+\"  NOT  pattern = \"\\\\d+\"")
print("\n  This way:")
print("  * Your code is easier to read")
print("  * You don't forget backslashes")
print("  * Regex sees what you intend")
