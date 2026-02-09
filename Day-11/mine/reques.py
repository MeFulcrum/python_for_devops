# """
# Generate a readable list of top-level functions and classes (with their public methods)
# from the `requests` module for students.

# Run (Windows):p
#     py -3 seperate.py
# """

import inspect
import sys

try:
    import requests
except ModuleNotFoundError:
    sys.exit("requests is not installed. Install with: py -3 -m pip install requests")

def public_members(obj, predicate):
    return [name for name, member in inspect.getmembers(obj, predicate) if not name.startswith("_")]

# Top-level functions in requests
functions = public_members(requests, inspect.isfunction)

# Top-level classes in requests
classes = [(name, cls) for name, cls in inspect.getmembers(requests, inspect.isclass) if cls.__module__.startswith('requests')]

lines = []
lines.append("Top-level functions in requests:")
for name in sorted(functions):
    lines.append(f" - {name}")

lines.append("\nTop-level classes in requests (with public methods):")
for cls_name, cls in sorted(classes, key=lambda x: x[0]):
    lines.append(f"\nClass: {cls_name}")
    methods = public_members(cls, inspect.isfunction)
    if not methods:
        lines.append("  (no public methods)")
    else:
        for m in sorted(methods):
            lines.append(f"  - {m}")
"""
Generate a readable list of top-level functions and classes (with their public methods)
from the `requests` module for students.

Run (Windows):
    py -3 reques.py
"""

import inspect
import sys

try:
    import requests
except ModuleNotFoundError:
    sys.exit("requests is not installed. Install with: py -3 -m pip install requests")

def public_members(obj, predicate):
    return [name for name, member in inspect.getmembers(obj, predicate) if not name.startswith("_")]

# Top-level functions in requests
functions = public_members(requests, inspect.isfunction)

# Top-level classes in requests
classes = [(name, cls) for name, cls in inspect.getmembers(requests, inspect.isclass) if cls.__module__.startswith('requests')]

lines = []
lines.append("Top-level functions in requests:")
for name in sorted(functions):
    lines.append(f" - {name}")

lines.append("\nTop-level classes in requests (with public methods):")
for cls_name, cls in sorted(classes, key=lambda x: x[0]):
    lines.append(f"\nClass: {cls_name}")
    methods = public_members(cls, inspect.isfunction)
    if not methods:
        lines.append("  (no public methods)")
    else:
        for m in sorted(methods):
            lines.append(f"  - {m}")

output = "\n".join(lines)

# Print to console and save to file for students
print(output)

with open("requests_api_list.txt", "w", encoding="utf-8") as f:
    f.write(output)