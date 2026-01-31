import re

search =  re.search(r'\d+', 'abc123def654')
if search:
    print("searched string is ",search.group())


if search:
    print(search.groups())

if search:
    print(search.group(0))

if search:
    print("start index of searched string", search.start())

if search:
    print("end index of a searched string", search.end())

if search:
    print("start and end of matched string", search.span())

text = "123 abc"

print("search detecting ", re.search(r"\d+", text).group())  # 123 (matches anywhere)
print("match at the start only from 123 abd", re.match(r"\d+", text).group())   # 123 (matches at start)

print("search finds string anywhere", re.search(r"abc", text).group())  # abc (matches anywhere)
print("match can only detect at the start", re.match(r"abc", text))           # None (not at start)

numbers = re.findall(r'\d+', 'a1b22c3333')
print("find all numbers",numbers)

for match in re.finditer(r'\d+', 'av4561ad55vf333'):
    print(match.group())

new_str = re.sub(r'\d+', '#', 'a1b22c333000')
print("sub function replaces number with hash",new_str)

parts = re.split(r'\d+', 'a1b22c333d4')
print("split string by occurances",parts)
