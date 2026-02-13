
class Character:
    def __init__(self, health, wealth, power):
        self.health = health
        self.wealth = wealth
        self.power = power

    def doubleSpeed(self):
        self.speed = 2 * self.speed
    
    def doublePower(self):
        self.power += self.power


warrior = Character(100, 12, 3)
ninga = Character(20, 30, 4)

print( "warrior" , str(warrior))
print("warrior speed", (warrior.health))
#returns the string representation of the object. If the class does not define a __str__ method, it will return a default string that includes the class name and memory address.
#output : warrior <__main__.Character object at 0x0000021B8
#output : warrior speed 100

print("ninja", ninga)
print("ninja pwoer", (ninga.power))
#returns the string representation of the object. If the class does not define a __str__ method, it will return a default string that includes the class name and memory address.
#output : warrior <__main__.Character object at 0x0000021B8

ninga.doublePower()

print("After double power", (ninga.power))
#returns the value of the named attribute of an object. If not found, it returns the default value provided (in this case, 'Not Found').
#output : After double power 8

print("Is warrior double speed callable?", callable(warrior.doubleSpeed))
#returns True if the object appears callable (i.e., it can be called like a function), otherwise returns False.
#output : Is warrior double speed callable? True

print("Is warrior power callable?", callable(warrior.power))
#returns True if the object appears callable (i.e., it can be called like a function), otherwise returns False.
#output : Is warrior double speed callable? True
#output : Is warrior power callable? False

print("Does warrior have double speed?", hasattr(warrior, 'doubleSpeed'))

print("Does warrior have power?", hasattr(warrior, 'power'))
#returns True if the object has the specified attribute, otherwise returns False.
#output : Does warrior have double speed? True
#output : Does warrior have power? True

print("Get attribute double speed of warrior", getattr(warrior, 'doubleSpeed', 'Not Found') )
#returns the value of the named attribute of an object. If not found, it returns the default value provided (in this case, 'Not Found').
#output : Get attribute double speed of warrior <bound method Character.doubleSpeed of <__main__.Character object at 0x0000021B8C9F3A30>>
print("Get attribute power of warrior", getattr(warrior, 'power', 'Not Found') )
#output : Get attribute power of warrior 3
#returns the value of the named attribute of an object. If not found, it returns the default value provided (in this case, 'Not Found').

#setattr(warrior, 'doubleSpeed', 10)
setattr(warrior, 'doubleSpeed', lambda: 10)
print("Get attribute double speed of warrior after setting it to 10", getattr(warrior, 'doubleSpeed', 'Not Found') )
#returns the value of the named attribute of an object. If not found, it returns the default value provided (in this case, 'Not Found').
#output : Get attribute double speed of warrior after setting it to 10 <function <lambda> at 0x0000021B8C9F3AF0>


#types of attributes in python
#1. Instance attributes: These are attributes that are specific to an instance of a class.

A = type(warrior)
print("Type of warrior", A)

a =isinstance(warrior, Character)
print("Is warrior an instance of Character?", a)
#returns True if the object is an instance of the specified class or a subclass thereof, otherwise returns False.
#ouput : Is warrior an instance of Character? True

b = isinstance(warrior, object)
print("Is warrior an instance of object?", b)
#returns True if the object is an instance of the specified class or a subclass thereof, otherwise returns False.
#output : Is warrior an instance of object? True
#output : Type of warrior <class '__main__.Character'>

