
def numberiseven(num):
    if num % 2 == 0:
        return "Number is even"
    else:
        return "Number is odd"
    
def numberisprime(num):
    if num <= 1:
        return "Number is not prime"
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return "Number is not prime"
    return "Number is prime"

