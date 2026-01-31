"""
Understanding Python String Prefixes: r, f, b, u and combinations

When you write a string literal in Python, you can prefix it with special characters
that change how Python interprets the string contents.
"""

# ==============================================================================
# THE 'r' PREFIX: RAW STRINGS
# ==============================================================================
# Purpose: Treats backslashes (\) literally instead of as escape characters.
# Common use: Regular expressions, file paths on Windows, etc.

print("=== RAW STRINGS (r prefix) ===\n")

# WITHOUT r: backslash is treated as escape character
normal_string = "line1\nline2"  # \n is interpreted as newline
print("Normal string:", repr(normal_string))
print("Printed:", normal_string)

# WITH r: backslash is literal (not an escape)
raw_string = r"line1\nline2"  # \n stays as literal backslash-n
print("\nRaw string:", repr(raw_string))
print("Printed:", raw_string)

# WHY 'r' is useful for regex patterns:
import re

# Without r: You'd need to escape backslashes
pattern_normal = "\\d+"  # Need to escape the backslash to get \d
print("\nPattern (normal):", repr(pattern_normal))

# With r: Write the pattern naturally
pattern_raw = r"\d+"  # Directly write what regex expects: \d+
print("Pattern (raw):", repr(pattern_raw))

# Both patterns work the same for regex
text = "I have 42 apples"
print("Matches with normal pattern:", re.findall(pattern_normal, text))
print("Matches with raw pattern:", re.findall(pattern_raw, text))

# Practical example: your original question
pattern_brown = r"brown:"
print("\nYour example pattern:", repr(pattern_brown))
print("This pattern looks for the literal text 'brown:' in a string")

# ==============================================================================
# OTHER STRING PREFIXES
# ==============================================================================

print("\n=== OTHER STRING PREFIXES ===\n")

# 1. 'f' PREFIX: F-STRING (format string) - Python 3.6+
# Purpose: Embed expressions directly in the string using {var_name}
name = "Alice"
age = 25
f_string = f"Name: {name}, Age: {age}"
print(f"f-string: {repr(f_string)}")
print(f"Printed: {f_string}")

# 2. 'b' PREFIX: BYTES
# Purpose: Creates a bytes object instead of a string
# Used for: binary data, file operations, network protocols
bytes_string = b"hello"
print(f"\nb-string: {repr(bytes_string)}")
print(f"Type: {type(bytes_string)}")
print(f"Printed: {bytes_string}")

# 3. 'u' PREFIX: UNICODE (mostly for Python 2 compatibility)
# Purpose: In Python 3, all strings are Unicode by default, so this does nothing.
#          Used in Python 2 to distinguish Unicode strings from byte strings.
unicode_string = u"hello"  # In Python 3, same as "hello"
print(f"\nu-string: {repr(unicode_string)}")
print(f"Type: {type(unicode_string)}")

# ==============================================================================
# COMBINING PREFIXES
# ==============================================================================

print("\n=== COMBINING PREFIXES ===\n")

# 'fr' or 'rf': Raw f-string (Python 3.6+)
# Combines: f-string + raw string
path = r"C:\Users\Bob"
fr_string = fr"File path: {path}"
print(f"fr-string: {repr(fr_string)}")
print(f"Printed: {fr_string}")

# 'br' or 'rb': Raw bytes
# Combines: bytes + raw string
raw_bytes = br"C:\Windows\System32"
print(f"\nbr-string: {repr(raw_bytes)}")
print(f"Type: {type(raw_bytes)}")

# ==============================================================================
# REGEX EXAMPLES WITH 'r' PREFIX
# ==============================================================================

print("\n=== REGEX PATTERN EXAMPLES WITH r PREFIX ===\n")

text = "My email is john@example.com and phone is 555-1234"

# Pattern 1: Find numbers
pattern1 = r"\d+"
matches1 = re.findall(pattern1, text)
print(f"Pattern: {repr(pattern1)}")
print(f"Matches: {matches1}\n")

# Pattern 2: Find email-like patterns
pattern2 = r"\w+@\w+\.\w+"
matches2 = re.findall(pattern2, text)
print(f"Pattern: {repr(pattern2)}")
print(f"Matches: {matches2}\n")

# Pattern 3: Your example - find "brown:" followed by optional whitespace
text_brown = "brown: the color brown: and BROWN: mixed case"
pattern3 = r"brown:"
matches3 = re.findall(pattern3, text_brown)
print(f"Pattern: {repr(pattern3)}")
print(f"Matches: {matches3}")
print(f"Note: This pattern is case-sensitive (matches only 'brown:', not 'BROWN:')\n")

# To make it case-insensitive, use re.IGNORECASE flag
matches3_ci = re.findall(pattern3, text_brown, re.IGNORECASE)
print(f"With re.IGNORECASE: {matches3_ci}")

# ==============================================================================
# SUMMARY TABLE
# ==============================================================================

print("\n=== SUMMARY TABLE ===\n")
print("Prefix  | Purpose                          | Example")
print("--------|----------------------------------|-----------")
print("(none)  | Normal string                    | \"hello\"")
print("r       | Raw string (literals backslash)  | r\"C:\\path\"")
print("f       | F-string (embed expressions)     | f\"Value: {x}\"")
print("b       | Bytes object                     | b\"hello\"")
print("u       | Unicode (Python 2 compat, no-op) | u\"hello\"")
print("fr/rf   | Raw f-string                     | fr\"Path: {x}\\n\"")
print("br/rb   | Raw bytes                        | br\"C:\\path\"")

print("\n=== KEY TAKEAWAY ===")
print("For REGEX patterns in Python, ALWAYS use r prefix!")
print("This prevents Python from interpreting backslashes as escape chars,")
print("and lets regex see the pattern exactly as you write it.")
