# ============================================================
# EXAMPLE 1: isinstance() - Check if object is instance of class
# ============================================================
class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()
cat = Cat()
string = "hello"

print("=== isinstance() Examples ===")
print(isinstance(dog, Dog))           # True
print(isinstance(dog, Animal))        # True (checks inheritance)
print(isinstance(cat, Dog))           # False
print(isinstance(string, str))        # True
print(isinstance(5, int))             # True
print()

# ============================================================
# EXAMPLE 2: type() - Get exact type of object
# ============================================================
print("=== type() Examples ===")
print(type(dog))                      # <class '__main__.Dog'>
print(type(dog).__name__)             # 'Dog'
print(type(cat))                      # <class '__main__.Cat'>
print(type(string))                   # <class 'str'>
print(type([1, 2, 3]))               # <class 'list'>
print(type({'a': 1}))                # <class 'dict'>
print()

# ============================================================
# EXAMPLE 3: dir() - List all attributes and methods
# ============================================================
class Person:
    def __init__(self, name):
        self.name = name
        self.age = 30
    
    def greet(self):
        return f"Hello, I'm {self.name}"
    
    def introduce(self):
        return f"I'm {self.age} years old"

person = Person("Alice")

print("=== dir() Examples ===")
print(dir(person))  # Shows all attributes and methods
print()
# You can filter to show only custom attributes
custom_attrs = [attr for attr in dir(person) if not attr.startswith('_')]
print("Custom attributes only:", custom_attrs)
print()

# ============================================================
# EXAMPLE 4: getattr() - Get attribute dynamically
# ============================================================
print("=== getattr() Examples ===")
print(getattr(person, 'name'))                    # Alice
print(getattr(person, 'age'))                     # 30
print(getattr(person, 'greet')())                # Hello, I'm Alice
print(getattr(person, 'unknown', 'Default'))     # Default (if doesn't exist)
print()

# ============================================================
# EXAMPLE 5: setattr() - Set attribute dynamically
# ============================================================
print("=== setattr() Examples ===")
print(f"Before: {person.name}")      # Alice
setattr(person, 'name', 'Bob')
print(f"After: {person.name}")       # Bob

# Create new attribute that didn't exist
setattr(person, 'email', 'bob@example.com')
print(f"New attribute: {person.email}")
print()

# ============================================================
# EXAMPLE 6: delattr() - Delete attribute dynamically
# ============================================================
class Student:
    def __init__(self):
        self.name = "Charlie"
        self.grade = "A"
        self.parent_contact = "123-456-7890"

student = Student()
print("=== delattr() Examples ===")
print(f"Before: {getattr(student, 'parent_contact')}")
delattr(student, 'parent_contact')
print(f"After deletion: {getattr(student, 'parent_contact', 'Not found')}")
print()

# ============================================================
# EXAMPLE 7: vars() - Get object's __dict__
# ============================================================
class Account:
    def __init__(self, username, balance):
        self.username = username
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount

account = Account("john_doe", 1000)

print("=== vars() Examples ===")
print(vars(account))  # {'username': 'john_doe', 'balance': 1000}
print()

# Modifying via vars()
account_dict = vars(account)
account_dict['balance'] = 2000
print(f"Updated balance: {account.balance}")  # 2000
print()

# ============================================================
# EXAMPLE 8: isinstance() vs type() - Key Difference
# ============================================================
print("=== isinstance() vs type() ===")

class Vehicle:
    pass

class Car(Vehicle):
    pass

my_car = Car()

# type() checks EXACT type
print(f"type(my_car) == Car: {type(my_car) == Car}")       # True
print(f"type(my_car) == Vehicle: {type(my_car) == Vehicle}")  # False

# isinstance() respects inheritance
print(f"isinstance(my_car, Car): {isinstance(my_car, Car)}")          # True
print(f"isinstance(my_car, Vehicle): {isinstance(my_car, Vehicle)}")  # True
print()

# ============================================================
# EXAMPLE 9: Dynamic method calling and attribute checking
# ============================================================
class Calculator:
    def add(self, a, b):
        return a + b
    
    def multiply(self, a, b):
        return a * b

class Logger:
    pass

def execute_operation(obj, method_name, *args):
    """Dynamically call a method if it exists"""
    if hasattr(obj, method_name):
        method = getattr(obj, method_name)
        if callable(method):
            return method(*args)
    return None

calc = Calculator()
logger = Logger()

print("=== Dynamic Method Calling ===")
print(execute_operation(calc, 'add', 5, 3))        # 8
print(execute_operation(calc, 'multiply', 4, 5))   # 20
print(execute_operation(logger, 'add', 5, 3))      # None (logger has no add method)
print()

# ============================================================
# EXAMPLE 10: Checking object properties dynamically
# ============================================================
class Document:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.read_only = False
    
    def save(self):
        return "Document saved"

class Image:
    def __init__(self, filename):
        self.filename = filename

doc = Document("My Doc", "Some content")
img = Image("photo.jpg")

print("=== Checking Object Properties ===")

# Check if object is writable (has read_only attribute and it's False)
def is_writable(obj):
    if hasattr(obj, 'read_only'):
        return not obj.read_only
    return True

print(f"Document is writable: {is_writable(doc)}")  # True
print(f"Image is writable: {is_writable(img)}")     # True (no read_only attr)

# Check if object has all required methods
required_methods = ['save']
def has_required_methods(obj, methods):
    for method in methods:
        if not (hasattr(obj, method) and callable(getattr(obj, method))):
            return False
    return True

print(f"Document has save method: {has_required_methods(doc, ['save'])}")  # True
print(f"Image has save method: {has_required_methods(img, ['save'])}")     # False
print()

# ============================================================
# EXAMPLE 11: Introspection - Listing methods only
# ============================================================
class Service:
    def start(self):
        pass
    
    def stop(self):
        pass
    
    status = "running"

print("=== List Methods Only ===")
service = Service()
methods = [attr for attr in dir(service) 
           if callable(getattr(service, attr)) and not attr.startswith('_')]
print(f"Methods: {methods}")  # ['start', 'stop']
print()

# ============================================================
# EXAMPLE 12: Type checking with multiple types
# ============================================================
print("=== Type checking for multiple types ===")

def process_input(data):
    if isinstance(data, (int, float)):
        return f"Number: {data * 2}"
    elif isinstance(data, str):
        return f"String: {data.upper()}"
    elif isinstance(data, list):
        return f"List: {len(data)} items"
    else:
        return "Unknown type"

print(process_input(5))              # Number: 10
print(process_input(3.14))           # Number: 6.28
print(process_input("hello"))        # String: HELLO
print(process_input([1, 2, 3]))      # List: 3 items
print(process_input({'a': 1}))       # Unknown type
