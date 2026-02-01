import sys

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mult(a,b):
    return a * b

num1 = sys.argv[1]

operation = sys.argv[2]

num2 = sys.argv[3]

if operation == "add":
    print(add(int(num1), int(num2)))   # if int() is not passed then, the numbers is treated as string and concatenated
    #e.g. python calc_new.py 3 add 5 => 35 without int() but with int() => 8
elif operation == "sub":
    print(subtract(int(num1), int(num2)))
elif operation == "mult":
    print(mult(int(num1), int(num2)))
else:
    print("Unsupported operation") 


# Example usage:
# python calc_new.py 10 add 5 -> Output: 15
# python calc_new.py 10 sub 5 -> Output: 5
# python calc_new.py 10 mult 5 -> Output: 50
# python calc_new.py 10 div 5 -> Output: Unsupported operation