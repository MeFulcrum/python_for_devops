import re

text = "The quick brown fox brown slap brown"

# Example: numbered capturing groups
pattern = r"(quick) (brown) (fox)"
m = re.search(pattern, text)
if m:
    print("Full match (group()):", m.group())        # entire match == group(0)
    print("group(1):", m.group(1))                 # first capture
    print("group(2):", m.group(2))
    print("group(3):", m.group(3))
    print("groups():", m.groups())                 # tuple of all groups
    print("span(0):", m.span(0))                   # (start, end) of whole match
    print("span(2):", m.span(2))                   # span of group 2
else:
    print("No match for numbered groups pattern")

print()
# Example: named capturing groups
pattern_named = r"(?P<color>brown) (?P<animal>fox)"
m2 = re.search(pattern_named, text)
if m2:
    print("Named groups:")
    print("m2.group('color'):", m2.group('color'))
    print("m2.group('animal'):", m2.group('animal'))
    print("m2.groupdict():", m2.groupdict())
    print("lastindex:", m2.lastindex)
    print("lastgroup:", m2.lastgroup)
else:
    print("No match for named-groups pattern")

# Notes:
# - Use m.group(n) for numbered groups, m.group('name') for named groups.
# - m.groups() -> tuple of all numbered groups (1..n)
# - m.groupdict() -> dict of named groups
# - m.span(n), m.start(n), m.end(n) give match positions
# - re.search() returns the first match as a Match object; re.findall() returns a list of strings/tuples
