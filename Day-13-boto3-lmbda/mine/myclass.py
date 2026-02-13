class Animal:
    def speak(s):
        print("Bark")

class Dog(Animal):
    def bark(s):
        print("Woof")

class Kingdom(Animal):
    def __init__(self, name):
        print("Kingdom name is", name)

d = Dog()
d.bark()
d.speak()

print(callable(d.speak))

print(callable(d.bark))

print(hasattr(d, 'speak'))
print(hasattr(d, 'bark'))

k = Kingdom("Animalia")


