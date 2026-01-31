"""
Demonstrations of common string-replacement techniques in Python.

This file shows:
- `str.replace()` (with `count`)
- `re.sub()` and `re.subn()` (regex-based replacements)
- `str.translate()` with `str.maketrans()` (character-wise replacements/deletions)
- `bytes.replace()` for byte-strings
- `split()` + `join()` and chained `replace()` as alternatives

Notes are provided inline with examples to make behaviour clear.
"""

import re


def basic_replace():
	s = "hello world hello blah blah hello"
	# Replace all occurrences
	all_replaced = s.replace("hello", "hi")
	# Replace only first occurrence (use count=1)
	first_only = s.replace("hello", "hi", 2)
	return s, all_replaced, first_only


def chained_replace():
	s = "apples, oranges, bananas"
	# Chaining multiple replace calls is simple but can be inefficient
	out = s.replace("apples", "pears").replace("oranges", "grapes")
	return s, out


def split_join_replace():
	s = "a--b--c"
	# For single-character or delimiter-based substitutions, split+join works.
	out = " ".join(s.split("--"))
	out2 = s.replace("--", " ")
	print("out2 (replace):", out2)
	# Note: this is often slower than str.replace for simple replacements.
	return s, out


def regex_replace():
	"""
	Demonstrate regex-based string replacements using re.sub() and re.subn().
	
	Key concepts:
	- re.sub(pattern, repl, string) finds all matches of 'pattern' (regex) and
	  replaces them with 'repl' (string or function).
	- The 'repl' argument can be:
	  a) A string: used as-is for all matches.
	  b) A callable (function): called with a Match object for each match.
	     The return value from the function replaces that match.
	- re.subn() is identical to re.sub() but returns a tuple: (new_string, count)
	  where 'count' is the number of replacements made.
	- Regex alternation (|) matches any of the patterns: "cat|bat" matches "cat" OR "bat".
	"""
	s = "cat bat rat"
	
	# Example 1: Simple string replacement with regex pattern
	# The pattern r"cat|bat" means: match either 'cat' OR 'bat'
	# All matches are replaced with "pet"
	out = re.sub(r"cat|bat", "pet", s)
	# Result: "pet pet rat" (both 'cat' and 'bat' are replaced)
	
	# Example 2: Function-based replacement (custom logic per match)
	# This is powerful when different matches need different replacements.
	repl_map = {"cat": "feline", "bat": "winged"}

	def repl_fn(m):
		# m is a Match object; m.group(0) returns the matched text
		# Look up the matched word in our map and return the replacement
		return repl_map.get(m.group(0), m.group(0))
		# .get(..., m.group(0)) means: if not found, return the original match unchanged

	out_fn = re.sub(r"cat|bat", repl_fn, s)
	# Result: "feline winged rat" (each word mapped to its custom replacement)
	
	# Example 3: Using re.subn() to also get the count of replacements
	# re.subn() returns (new_string, number_of_substitutions)
	out_n = re.subn(r"cat|bat", "pet", s)
	# out_n = ('pet pet rat', 2)  # 2 replacements were made
	
	return s, out, out_fn, out_n


def translate_example():
	"""
	Demonstrate character-level replacements and deletions using str.translate().
	
	Key concepts:
	- str.translate(table) uses a translation table to perform efficient
	  character-by-character transformations on a string.
	- str.maketrans() creates the translation table. It has two forms:
	  a) str.maketrans(x, y) maps each char in 'x' to the char at same index in 'y'.
	  b) str.maketrans({char: replacement, ...}) maps chars to strings/None.
	- Mapped to None: deletes that character from the result.
	- Unlike str.replace(), translate() is very fast for many replacements.
	- Drawback: each replacement is character-to-character or char-to-string;
	  use re.sub() for complex substring patterns.
	"""
	s = "hello 123"
	
	# Example 1: Character mapping with replacements
	# Create a mapping dict: each key char maps to its replacement value (can be a string)
	table = str.maketrans({"h": "H", "1": "one", " ": "_"})
	out = s.translate(table)
	# 'h' -> 'H', '1' -> 'one', ' ' -> '_'
	# Result: "Hello_one23" (note: only 'h' and '1' and ' ' from the dict are replaced)
	
	# Example 2: Character deletion using str.maketrans("", "", delchars)
	# The third argument to str.maketrans specifies characters to delete
	table_del = str.maketrans("", "", "123")
	out_del = s.translate(table_del)
	# Deletes all occurrences of '1', '2', '3'
	# Result: "hello " (digits removed, space remains)
	
	return s, out, out_del


def bytes_replace_example():
	"""
	Demonstrate string replacement on bytes objects (binary data).
	
	Key concepts:
	- bytes objects are immutable sequences of bytes (0-255 integer values).
	- bytes.replace(old, new) works identically to str.replace().
	- Both 'old' and 'new' must be bytes literals (b'...' notation).
	- Use bytes when working with binary files, network protocols, encodings, etc.
	- The count argument works the same way: bytes.replace(old, new, count).
	- Each byte is a value from 0-255; \x00 is the null byte (value 0).
	"""
	b = b"foo\x00bar\x00foo"
	# Note: \x00 is the null byte (binary 0), commonly found in binary data.
	# This could represent a C-style null-terminated string split into two parts.
	
	# Replace all null bytes (\x00) with underscores (_)
	# Both arguments must be bytes objects (prefixed with b)
	out = b.replace(b"\x00", b"_")
	# Result: b"foo_bar_foo"
	# Notice: replacement works at byte level; if you replace with a longer byte
	# sequence, the result is longer. E.g., b.replace(b"foo", b"FOOD") would
	# create a longer bytes object.
	
	return b, out


def important_notes():
	notes = [
		"Strings are immutable: all replace functions return new strings.",
		"str.replace(old, new, count=-1) replaces up to `count` occurrences;"
		" default is -1 (replace all).",
		"re.sub(pattern, repl, string) uses regex - it's more powerful but slower.",
		"str.translate() is efficient for character-level replacements/deletions.",
		"When replacing multiple different substrings, consider regex or a mapping function",
	]
	return notes


def show_examples():
	print("-- basic_replace --")
	s, allr, first = basic_replace()
	print("original:", s)
	print("all replaced:", allr)
	print("first only:", first)

	print("\n-- chained_replace --")
	s, out = chained_replace()
	print(s, "->", out)

	print("\n-- split_join_replace --")
	s, out = split_join_replace()
	print(s, "->", out)

	print("\n-- regex_replace --")
	s, out, out_fn, out_n = regex_replace()
	print("pattern replace:", out)
	print("function replace:", out_fn)
	print("re.subn result:", out_n)

	print("\n-- translate_example --")
	s, out, out_del = translate_example()
	print(s, "->", out)
	print("deleted chars:", out_del)

	print("\n-- bytes_replace_example --")
	b, bout = bytes_replace_example()
	print(b, "->", bout)

	print("\n-- notes --")
	for n in important_notes():
		print("-", n)


if __name__ == '__main__':
	show_examples()

