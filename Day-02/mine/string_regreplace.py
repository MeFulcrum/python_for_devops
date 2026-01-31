import re

str = "foo bar foo baz foo"

def regex_replace():
    out = re.sub(r"foo", "qux", str)
    return out

print("Original string:", str)
print("After regex replace:", regex_replace())

def reg_functionreplace():
    repl_map = {"foo": "fucked", "baz": "winged"}

    def replace_func(match):
        return repl_map.get(match.group(0), match.group(0))

    out = re.sub(r"foo|baz", replace_func, str)
    return out

print("Replacement map:", reg_functionreplace())

#use startswith() to check if string starts with a specific substring
def starts_with(substring):
    return str.startswith(substring)    

print("Does the string start with 'foo'? :", starts_with("foos"))