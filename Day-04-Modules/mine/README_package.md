# mine/my_package 📦

This folder contains a simple example Python package named `my_package` created as an exercise for Day-04 (Functions, Modules and Packages).

Structure:

```
mine/
  ├─ my_package/
  │    ├─ __init__.py   # exposes `greet` and `square`
  │    ├─ module1.py    # greet(name)
  │    └─ module2.py    # square(x)
  └─ example_usage.py   # shows how to import and use the package
```

Usage:

- From the `mine/` directory run:

```bash
python example_usage.py
```

- Or import from other scripts:

```python
from my_package import greet, square

print(greet("Alice"))
print(square(5))
```

This follows the packages guidance from the Day-04 `README.md` (a package is a directory with `__init__.py` and contains modules you can import). ✅
