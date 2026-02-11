"""
DICTIONARY METHODS AND OPERATIONS GUIDE
Complete reference for working with dictionaries in Python
Run: python dictionary_methods_guide.py
"""

print("=" * 80)
print("PYTHON DICTIONARY METHODS & OPERATIONS GUIDE")
print("=" * 80)

# ============================================================================
# 1. CREATING DICTIONARIES
# ============================================================================
print("\n[1] CREATING DICTIONARIES")
print("-" * 80)

# Method 1: Literal syntax
d1 = {'name': 'Alice', 'age': 30, 'city': 'NYC'}
print(f"Literal syntax: {d1}")

# Method 2: dict() constructor
d2 = dict(name='Bob', age=25, city='LA')
print(f"dict() constructor: {d2}")

# Method 3: dict from list of tuples
d3 = dict([('x', 10), ('y', 20), ('z', 30)])
print(f"From list of tuples: {d3}")

# ============================================================================
# 2. ACCESSING & CHECKING KEYS
# ============================================================================
print("\n[2] ACCESSING & CHECKING KEYS")
print("-" * 80)

person = {'name': 'Charlie', 'age': 28, 'job': 'Engineer'}

print(f"Dict: {person}")
print(f"person['name'] = {person['name']}")
print(f"person.get('age') = {person.get('age')}")
print(f"person.get('salary', 'Unknown') = {person.get('salary', 'Unknown')}")
print(f"salary in person = {'salary' in person}")
print(f"'name' in person = {'name' in person}")
print(f"'salary' in person = {'salary' in person}")

# ============================================================================
# 3. ALL DICTIONARY METHODS
# ============================================================================
print("\n[3] ALL DICTIONARY METHODS")
print("-" * 80)

sample_dict = {'a': 1, 'b': 2, 'c': 3}

# 1. keys() - Return all keys
print(f"\n1. keys()")
print(f"   Returns: {sample_dict.keys()}")
print(f"   Type: {type(sample_dict.keys())}")
print(f"   As list: {list(sample_dict.keys())}")

# 2. values() - Return all values
print(f"\n2. values()")
print(f"   Returns: {sample_dict.values()}")
print(f"   As list: {list(sample_dict.values())}")

# 3. items() - Return (key, value) tuples
print(f"\n3. items()")
print(f"   Returns: {sample_dict.items()}")
for key, val in sample_dict.items():
    print(f"      Key: {key}, Value: {val}")

# 4. get(key, default) - Get value with default
print(f"\n4. get(key, default=None)")
print(f"   sample_dict.get('a' , 'default') = {sample_dict.get('a', 'default')}")
print(f"   sample_dict.get('z', 'not found') = {sample_dict.get('z', 'not found')}")

# 5. pop(key, default) - Remove and return value
test_dict = {'x': 10, 'y': 20}
print(f"\n5. pop(key, default=None)")
print(f"   Before: {test_dict}")
val = test_dict.pop('x', 'missing')
print(f"   test_dict.pop('x') returned: {val}")
print(f"   After: {test_dict}")

# 6. popitem() - Remove and return last (key, value)
test_dict = {'a': 1, 'b': 2, 'c': 3}
print(f"\n6. popitem()")
print(f"   Before: {test_dict}")
item = test_dict.popitem()
print(f"   Removed: {item}")
print(f"   After: {test_dict}")

# 7. clear() - Remove all items
test_dict = {'a': 1, 'b': 2}
print(f"\n7. clear()")
print(f"   Before: {test_dict}")
test_dict.clear()
print(f"   After: {test_dict}")

# 8. update(dict) - Merge or update with another dict
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'a': 10}
print(f"\n8. update(dict)")
print(f"   dict1 before: {dict1}")
print(f"   dict2: {dict2}")
dict1.update(dict2)
print(f"   dict1 after update: {dict1}")

# 9. copy() - Shallow copy
original = {'x': 1, 'y': 2}
print(f"\n9. copy()")
print(f"   Original: {original}")
copied = original.copy()
copied['x'] = 999
print(f"   After modifying copy - Original: {original}, Copy: {copied}")

# 10. fromkeys(keys, value) - Create dict from keys
print(f"\n10. fromkeys(keys, value)")
keys = ['red', 'green', 'blue']
colors = dict.fromkeys(keys, 0)
print(f"    dict.fromkeys({keys}, 0) = {colors}")

# 11. setdefault(key, default) - Get key or set if missing
test_dict = {'a': 1}
print(f"\n11. setdefault(key, default=None)")
print(f"    test_dict: {test_dict}")
val1 = test_dict.setdefault('a', 100)
print(f"    test_dict.setdefault('a', 100) = {val1}")
val2 = test_dict.setdefault('b', 200)
print(f"    test_dict.setdefault('b', 200) = {val2}")
print(f"    test_dict after: {test_dict}")

# 12. len() - Number of items
print(f"\n12. len() - Get number of items")
d = {'a': 1, 'b': 2, 'c': 3}
print(f"    len({d}) = {len(d)}")

# 13. str() / repr() - String representation
print(f"\n13. str() / repr() - Convert to string")
d = {'name': 'Alice', 'age': 30}
print(f"    str({d}) = {str(d)}")

# ============================================================================
# 4. ITERATING THROUGH DICTIONARIES
# ============================================================================
print("\n[4] ITERATING THROUGH DICTIONARIES")
print("-" * 80)

data = {'fruit': 'apple', 'color': 'red', 'count': 5}

# Iterate over keys
print(f"\nIterating over keys:")
for key in data:
    print(f"  {key}")

# Iterate over values
print(f"\nIterating over values:")
for val in data.values():
    print(f"  {val}")

# Iterate over items
print(f"\nIterating over items:")
for key, val in data.items():
    print(f"  {key}: {val}")

# ============================================================================
# 5. DICTIONARY COMPREHENSION
# ============================================================================
print("\n[5] DICTIONARY COMPREHENSION")
print("-" * 80)

# Simple comprehension
d1 = {x: x**2 for x in range(1, 6)}
print(f"Squares: {d1}")

# With condition
d2 = {x: x**2 for x in range(1, 10) if x % 2 == 0}
print(f"Even squares: {d2}")

# From two lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]
d3 = {k: v for k, v in zip(keys, values)}
print(f"From lists: {d3}")

# ============================================================================
# 6. NESTED DICTIONARIES
# ============================================================================
print("\n[6] NESTED DICTIONARIES")
print("-" * 80)

students = {
    'student1': {'name': 'Alice', 'age': 20, 'grade': 'A'},
    'student2': {'name': 'Bob', 'age': 21, 'grade': 'B'},
    'student3': {'name': 'Charlie', 'age': 22, 'grade': 'A'}
}

print(f"Nested dict: {students}")
print(f"Alice's grade: {students['student1']['grade']}")
print(f"\nAll students:")
for sid, info in students.items():
    print(f"  {sid}: {info['name']} (Grade: {info['grade']})")

# ============================================================================
# 7. HELPER CLASS FOR DICTIONARY OPERATIONS
# ============================================================================
print("\n[7] DICTIONARY HELPER CLASS")
print("-" * 80)

class DictionaryHelper:
    """A helper class to work with dictionaries easily"""
    
    def __init__(self):
        self.data = {}
    
    def add_entry(self, key, value):
        """Add a single key-value pair"""
        self.data[key] = value
        print(f"✓ Added: {key} = {value}")
    
    def add_multiple(self, **kwargs):
        """Add multiple entries at once"""
        self.data.update(kwargs)
        print(f"✓ Added {len(kwargs)} entries")
    
    def display(self):
        """Display all entries"""
        if not self.data:
            print("Dictionary is empty")
            return
        for key, val in self.data.items():
            print(f"  {key}: {val}")
    
    def search(self, key):
        """Search for a key"""
        if key in self.data:
            return self.data.get(key)
        return None
    
    def remove(self, key):
        """Remove an entry"""
        if key in self.data:
            del self.data[key]
            print(f"✓ Removed: {key}")
        else:
            print(f"✗ Key not found: {key}")
    
    def get_keys(self):
        """Get all keys"""
        return list(self.data.keys())
    
    def get_values(self):
        """Get all values"""
        return list(self.data.values())
    
    def count(self):
        """Count total entries"""
        return len(self.data)
    
    def clear_all(self):
        """Clear all entries"""
        self.data.clear()
        print("✓ Dictionary cleared")
    
    def merge(self, other_dict):
        """Merge with another dictionary"""
        self.data.update(other_dict)
        print(f"✓ Merged {len(other_dict)} items")
    
    def filter_by_value(self, value):
        """Find all keys with a specific value"""
        return [k for k, v in self.data.items() if v == value]
    
    def sort_by_key(self):
        """Get sorted dictionary by key"""
        return dict(sorted(self.data.items()))
    
    def sort_by_value(self):
        """Get sorted dictionary by value"""
        return dict(sorted(self.data.items(), key=lambda x: x[1]))


# ============================================================================
# 8. DEMO OF HELPER CLASS
# ============================================================================
print("\n[8] DEMO - USING THE HELPER CLASS")
print("-" * 80)

helper = DictionaryHelper()

print("\nAdding single entry:")
helper.add_entry('Python', 95)

print("\nAdding multiple entries:")
helper.add_multiple(JavaScript=88, Java=90, C=85, Rust=92)

print("\nCurrent dictionary:")
helper.display()

print(f"\nTotal entries: {helper.count()}")

print(f"\nAll keys: {helper.get_keys()}")
print(f"All values: {helper.get_values()}")

print(f"\nSearching for 'Java': {helper.search('Java')}")
print(f"Searching for 'Go': {helper.search('Go')}")

print(f"\nKeys with value 90: {helper.filter_by_value(90)}")

print("\nSorted by key:")
print(helper.sort_by_key())

print("\nSorted by value (scores):")
print(helper.sort_by_value())

print("\nRemoving 'C':")
helper.remove('C')

print("\nFinal dictionary:")
helper.display()

# ============================================================================
# 9. ADVANCED STUDENT DICTIONARY CLASS
# ============================================================================
print("\n[9] ADVANCED STUDENT CLASS WITH DICTIONARY")
print("-" * 80)

class StudentDatabase:
    """Database to manage student records"""
    
    def __init__(self):
        self.students = {}
    
    def add_student(self, student_id, name, age, grade):
        """Add a new student"""
        self.students[student_id] = {
            'name': name,
            'age': age,
            'grade': grade
        }
        print(f"✓ Student {student_id} added: {name}")
    
    def get_student(self, student_id):
        """Get student info"""
        return self.students.get(student_id, "Student not found")
    
    def update_grade(self, student_id, new_grade):
        """Update student's grade"""
        if student_id in self.students:
            self.students[student_id]['grade'] = new_grade
            print(f"✓ Grade updated for {student_id}")
        else:
            print(f"✗ Student {student_id} not found")
    
    def list_all_students(self):
        """List all students"""
        if not self.students:
            print("No students in database")
            return
        for sid, info in self.students.items():
            print(f"  {sid}: {info['name']}, Age: {info['age']}, Grade: {info['grade']}")
    
    def get_students_by_grade(self, grade):
        """Find students with specific grade"""
        return [sid for sid, info in self.students.items() if info['grade'] == grade]
    
    def count_students(self):
        """Total students"""
        return len(self.students)


# Demo
print("\nDemo - Student Database:")
db = StudentDatabase()
db.add_student('S001', 'Alice', 20, 'A')
db.add_student('S002', 'Bob', 21, 'B')
db.add_student('S003', 'Charlie', 22, 'A')
db.add_student('S004', 'Diana', 20, 'A')

print("\nAll Students:")
db.list_all_students()

print(f"\nStudents with grade A: {db.get_students_by_grade('A')}")
print(f"Total students: {db.count_students()}")

print("\nUpdating Bob's grade to A:")
db.update_grade('S002', 'A')

print("\nUpdated students with grade A: {db.get_students_by_grade('A')}")

print("\n" + "=" * 80)
print("END OF GUIDE")
print("=" * 80)
