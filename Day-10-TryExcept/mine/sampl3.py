
userinput = input("enter two numbers separated by space: ")
numbers = userinput.split()
print(f"Numbers entered: {numbers}")

#Adding two numbers
try:
    num1 = float(numbers[0])
    num2 = float(numbers[1])
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is: {result}")
except ValueError:
    print("Please enter valid numbers.")
except IndexError:
    print("Please enter two numbers separated by space.")
