"""
Simple examples showing how to use `str.strip()` (and friends).

Notes:
- `strip()`    : removes characters from both ends of the string. By
				 default it removes whitespace (spaces, tabs, newlines).
- `lstrip()`   : removes characters only from the left (leading) side.
- `rstrip()`   : removes characters only from the right (trailing) side.

You can also provide a string of characters to remove, e.g. `s.strip("*.")`
will remove any leading/trailing `*` or `.` characters (it does not remove
those characters from the middle of the string).

Run this file to see outputs demonstrating removal of whitespace
and removal of specific characters.
"""

def show_strip_examples():

    s = "   \t\n  Hello, World!  \n"
    print("Original:", repr(s))
    print("strip():", repr(s.strip()))
    print("lstrip():", repr(s.lstrip()))
    print("rstrip():", repr(s.rstrip()))

    # strip accepts an optional argument of characters to remove
    s2 = "***Impor***tant***"
    print("\nOriginal2:", repr(s2))
    print("strip('*'):", repr(s2.strip('*')))
    print("lstrip('*'):", repr(s2.lstrip('*')))
    print("rstrip('*'):", repr(s2.rstrip('*')))

    #split does not remove characters from the middle of the string
    s3 = "***Impor&&&tant***"
    print("\nOriginal3:", repr(s3))
    print("strip('&'):", repr(s3.strip('&')))
    print("lstrip('&'):", repr(s3.lstrip('&')))
    print("rstrip('&'):", repr(s3.rstrip('&')))

if __name__ == '__main__':
    show_strip_examples()

