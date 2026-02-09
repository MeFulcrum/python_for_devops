import inspect
import sys

try:
    import requests
except ModuleNotFoundError:
    sys.exit("requests is not installed. Install with: py -3 -m pip install requests")

def public_names(obj, predicate):
    return [name for name, member in inspect.getmembers(obj, predicate) if not name.startswith("_")]

functions = public_names(requests, inspect.isfunction)

classes = [
    (name, cls)
    for name, cls in inspect.getmembers(requests, inspect.isclass)
    if getattr(cls, "__module__", "").startswith("requests")
]

lines = []
lines.append("REQUESTS - FUNCTIONS")
lines.extend(sorted(functions))

lines.append("")
lines.append("REQUESTS - CLASSES AND PUBLIC METHODS")
for cls_name, cls in sorted(classes, key=lambda x: x[0]):
    lines.append(cls_name)
    methods = public_names(cls, inspect.isfunction)
    if methods:
        for m in sorted(methods):
            lines.append(f"  {m}")
    else:
        lines.append("  (no public methods)")

output = "\n".join(lines)
print(output)

with open("requests_api_list.txt", "w", encoding="utf-8") as f:
    f.write(output)