class Person:
    def __init__(self):
        self.name = "John"
        self.age = 30
    
    def greet(self):
        return "Hello!"

person = Person()

# Check for existing attribute
print(hasattr(person, 'name'))      # True
print(hasattr(person, 'age'))       # True
print(hasattr(person, 'greet'))     # True (methods are also attributes)

# Check for non-existing attribute
print(hasattr(person, 'address'))   # False
print(hasattr(person, 'unknown'))   # False
