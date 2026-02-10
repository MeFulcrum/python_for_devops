import re

text = "The quick brown fox"
pattern = r"quick"

"""
Demonstrate and explain `re.match()` and related regex matching functions.

Key points:
- `re.match(pattern, string)` checks for a match *only at the start* of the string.
- `re.search(pattern, string)` searches the entire string and returns the first match.
- `re.fullmatch(pattern, string)` requires the entire string to match the pattern.
- `re.findall()` returns a list of matches (no Match object).
- `re.finditer()` yields Match objects for all non-overlapping matches.

Use `r"..."` for regex patterns to avoid double-escaping backslashes.
"""

import re


text = "The quick brown fox"

# Example: re.match only matches at the beginning
pattern = r"quick"
m = re.match(pattern, text)
print("text:", text)
print("pattern:", pattern)
if m:
    print("re.match -> matched:", m.group())
else:
    print("re.match -> No match (pattern not at start)")


# Example: re.search finds the pattern anywhere
ms = re.search(pattern, text)
if ms:
    print("re.search -> matched:", ms.group())
    print("  span:", ms.span())
else:
    print("re.search -> No match")


# Example: re.fullmatch requires entire string to match
pattern_full = r"The quick brown fox"
mf = re.fullmatch(pattern_full, text)
print("re.fullmatch pattern:", repr(pattern_full))
print("re.fullmatch ->", "matched" if mf else "no match")


# Match object useful methods (when a match exists)
if ms:
    print("\nMatch object methods:")
    print("  group():", ms.group())        # whole match == group(0)
    # Demonstrate capture groups
    m_groups = re.search(r"(quick) (brown) (fox)", text)
    if m_groups:
        print("  groups():", m_groups.groups())
        print("  group(1):", m_groups.group(1))
        print("  start(0), end(0):", m_groups.start(0), m_groups.end(0))
        print("  span(2):", m_groups.span(2))
        print("  groupdict():", m_groups.groupdict())

    # expand(template) example: use backreferences \1 etc.
    print("  expand('\\1-\\2-\\3'):", m_groups.expand("\\1-\\2-\\3"))


# Other notes:
print("\nOther helpful functions:")
print(" - re.findall(pattern, text) -> returns list of matches (strings or tuples)")
print(" - re.finditer(pattern, text) -> yields Match objects for each match")
print(" - Use named groups (?P<name>...) and access via m.group('name') or m.groupdict()")
