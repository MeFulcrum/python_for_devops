"""
UNDERSTANDING groupdict()

What is groupdict()?
- groupdict() returns a DICTIONARY of all NAMED GROUPS in a regex match
- Keys are the group names you defined with (?P<name>...)
- Values are the matched text for each named group
- If a named group didn't match, its value is None (or default value if provided)

Why use it?
- Access matched parts by meaningful names instead of numbers
- Much clearer and more readable than group(1), group(2), etc.
- Useful for structured data extraction (emails, phone numbers, etc.)
"""

import re

print("=" * 70)
print("EXAMPLE 1: Simple Email Extraction")
print("=" * 70)

text = "Contact me at john.doe@example.com for more info"

# Pattern with named groups for email parts
pattern = r"(?P<user>\w+\.\w+)@(?P<domain>\w+\.\w+)"
m = re.search(pattern, text)

if m:
    print("\nText:", text)
    print("\nPattern:", pattern)
    print("\nMatched email:", m.group(0))
    
    print("\nUsing individual groups:")
    print("  m.group('user'):", m.group('user'))
    print("  m.group('domain'):", m.group('domain'))
    
    print("\nUsing groupdict() (much cleaner!):")
    print("  m.groupdict():", m.groupdict())
    
    # Easy to access like a dictionary
    d = m.groupdict()
    print("\nAccessing from dict:")
    print("  User part:", d['user'])
    print("  Domain part:", d['domain'])


print("\n" + "=" * 70)
print("EXAMPLE 2: Phone Number Extraction")
print("=" * 70)

text = "My phone is 555-123-4567"

# Pattern with named groups for phone parts
pattern = r"(?P<area>\d{3})-(?P<exchange>\d{3})-(?P<line>\d{4})"
m = re.search(pattern, text)

if m:
    print("\nText:", text)
    print("\nPattern:", pattern)
    
    print("\nUsing groupdict():")
    phone_dict = m.groupdict()
    print("  groupdict():", phone_dict)
    
    print("\nNow it's easy to use:")
    print("  Area code:", phone_dict['area'])
    print("  Exchange:", phone_dict['exchange'])
    print("  Line number:", phone_dict['line'])


print("\n" + "=" * 70)
print("EXAMPLE 3: HTML Tag Extraction")
print("=" * 70)

text = '<a href="https://example.com">Click here</a>'

# Pattern with named groups for HTML tag parts
pattern = r'<(?P<tag>\w+).*?href="(?P<url>[^"]+)"[^>]*>(?P<text>[^<]+)</\w+>'
m = re.search(pattern, text)

if m:
    print("\nText:", text)
    print("\nPattern:", pattern)
    
    print("\nUsing groupdict():")
    html_dict = m.groupdict()
    print("  groupdict():", html_dict)
    
    print("\nAccessing values:")
    print("  Tag:", html_dict['tag'])
    print("  URL:", html_dict['url'])
    print("  Text:", html_dict['text'])


print("\n" + "=" * 70)
print("EXAMPLE 4: Multiple Matches with finditer() and groupdict()")
print("=" * 70)

text = "Emails: alice@test.com, bob@test.com, charlie@test.org"

# Pattern with named groups
pattern = r"(?P<email_user>\w+)@(?P<domain>\w+\.\w+)"

print("\nText:", text)
print("\nPattern:", pattern)

print("\nFinding all matches and converting to dicts:")
for m in re.finditer(pattern, text):
    # Each match has groupdict()
    d = m.groupdict()
    print(f"  {d['email_user']:10} @ {d['domain']}")


print("\n" + "=" * 70)
print("EXAMPLE 5: Optional Groups (returns None if not matched)")
print("=" * 70)

text1 = "John Smith"
text2 = "Mary Johnson (age 28)"

# Pattern with optional group for age
pattern = r"(?P<first>\w+)\s(?P<last>\w+)(\s\(age\s(?P<age>\d+)\))?"

print("\nPattern:", pattern)

print("\nMatch 1: '" + text1 + "'")
m1 = re.search(pattern, text1)
if m1:
    d1 = m1.groupdict()
    print("  groupdict():", d1)
    print("  Note: 'age' is", d1['age'], "because it didn't match")

print("\nMatch 2: '" + text2 + "'")
m2 = re.search(pattern, text2)
if m2:
    d2 = m2.groupdict()
    print("  groupdict():", d2)
    print("  Note: 'age' is", d2['age'], "because it DID match")


print("\n" + "=" * 70)
print("KEY POINTS ABOUT groupdict()")
print("=" * 70)

print("""
1. groupdict() only works with NAMED GROUPS (?P<name>...)
   - Returns dict like {'name1': 'value1', 'name2': 'value2', ...}

2. For optional groups that don't match:
   - groupdict() returns None for that key
   - Use m.groupdict(default='') to change default value

3. Compare:
   - m.group(1)        -> returns value or None if doesn't exist
   - m.groups()        -> returns tuple of ALL numbered groups
   - m.groupdict()     -> returns dict of ALL named groups
   - m.group('name')   -> returns value of named group

4. Why use it?
   - MUCH MORE READABLE than m.group(1), m.group(2), ...
   - Easier to remember: 'email' vs group number 1
   - Self-documenting code
   - Easy to convert to JSON or database records
""")
