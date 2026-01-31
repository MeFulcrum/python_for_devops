import re

text = "The quick brown fox brown slap brown"
pattern = r"brown"
p1 = r"(brown) (fox)"
p2 = r"fox"
# r means raw string - backslashes are treated literally (not as escape characters) meaning special regex characters can be used without double-escaping.
# other options are patter= 
search = re.search(p1, text)
if search:
    print("Pattern found:", search.group(1)) # first capturing group
    print("2nd Pattern Found:", search.group(2)) #seacond captured group
    print("Full match:", search.group())  # entire match
    print("Groups:", search.groups()) # tuple of all capturing groups
    print("Span:", search.span()) # start and end indices of the match

    print("Start index of group 1:", search.start(1)) # start index of first capturing group
    print("End index of group 1:", search.end(1)) # end index of first capturing group
    print("Start index of group 2:", search.start(2)) # start index of second capturing group
    print("End index of group 2:", search.end(2)) # end index of second capturing group
    print("Group dict:", search.groupdict()) # dictionary of named capturing groups
    print("Last index:", search.lastindex) # index of last matched capturing group
    print("Last group name:", search.lastgroup) # name of last matched capturing group
else:
    print("Pattern not found")
