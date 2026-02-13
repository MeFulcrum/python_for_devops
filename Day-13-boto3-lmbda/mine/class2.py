def my_function():
    return "I'm a function"

class MyClass:
    def method(self):
        return "I'm a method"
    
    def __call__(self):
        return "I'm callable via __call__"

obj = MyClass()

# Functions and methods are callable #Callable means that the object can be called like a function, i.e., using parentheses.
print(callable(my_function))        # True
print(callable(obj.method))         # True
print(callable(MyClass))            # True (classes are callable)

# Objects with __call__ are callable
print(callable(obj))                # True

# Regular variables are NOT callable
x = 5
print(callable(x))                  # False
print(callable("string"))           # False
print(callable([1, 2, 3]))         # False