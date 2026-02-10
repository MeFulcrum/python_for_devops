
fruits = ["apple", "banana", "cherry"]

for fr in fruits:
    print("- ", fr)

for index in range(len(fruits)):
    print(f"Index {index} contains {fruits[index]}")

for i in range(5):
    print(f"Iteration {i}")

for i in range(2, 10, 2):
    print(f"Even number: {i}")

for char in "DevOps":
    print(f"Character: {char}")

for num in [1, 2, 3, 4, 5]:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

total = 0
for i in range(1, 6):
    total += i
print(f"Sum of first 5 natural numbers is {total}")

for fruit in fruits:
    if fruit == "banana":
        print("Found banana, stopping the search.")
        break
    print(f"Checked {fruit}")

for fruit in fruits:
    if fruit == "banana":
        print("Skipping banana.")
        continue
    print(f"Processing {fruit}")

for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
else:
    print("Completed all iterations.")  


count = 0 
while count < 5:
    print(f"Count is {count}")
    count += 1

n = 3
while n > 0:
    print(f"n is {n}")
    n -= 1

i = 0
while i < 5:
    if i == 3:
        print("Breaking at i=3")
        break
    print(f"i = {i}")
    i += 1

m = 0
while m < 5:
    m += 1
    if m == 2:
        print("Skipping m=2")
        continue
    print(f"m = {m}")


#While-else example
x = 0
while x < 3:
    print(f"x is {x}")
    x += 1
else:
    print("Finished counting x")
    
#While-else with break
y = 0
while y < 5:
    if y == 3:
        print("Breaking at y=3")
        break
    print(f"y = {y}")
    y += 1
else:
    print("Finished counting y")

# While-else with continue
z = 0
while z < 5:    
    z += 1
    if z == 2:
        print("Skipping z=2")
        continue
    print(f"z = {z}")
else:
    print("Finished counting z")

#While with nested for loop
a = 0
while a < 3:
    print(f"Outer loop a={a}")
    for b in range(2):
        print(f"  Inner loop b={b}")
    a += 1

#While with nested while loop
c = 0
while c < 3:    
    print(f"Outer loop c={c}")
    d = 0
    while d < 2:
        print(f"  Inner loop d={d}")
        d += 1
    c += 1

#While with nested for and while loop
e = 0
while e < 2:    
    print(f"Outer loop e={e}")
    for f in range(2):
        print(f"  For loop f={f}")
    g = 0
    while g < 2:
        print(f"  While loop g={g}")
        g += 1
    e += 1

#While loop with sleep 
import time
h = 0 
while h < 3:
    print(f"h is {h}")
    time.sleep(1)  # Sleep for 1 second
    h += 1

#While loop with user input
while True:
    user_input = input("Enter 'exit' to stop: ")
    if user_input.lower() == 'exit':
        print("Exiting the loop.")
        break
    else:
        print(f"You entered: {user_input}")

#While loop with a counter and a condition
counter = 0
while counter < 10:
    print(f"Counter is {counter}")
    counter += 1
    if counter == 5:
        print("Counter reached 5, breaking the loop.")
        break

#While loop with a flag
flag = True
while flag:
    print("Flag is True, continuing the loop.")
    user_input = input("Enter 'stop' to set flag to False: ")
    if user_input.lower() == 'stop':
        flag = False
        print("Flag set to False, exiting the loop.")

#While loop with a break and an else
i = 0
while i < 5:
    print(f"i is {i}")
    if i == 3:
        print("Breaking at i=3")
        break
    i += 1
else:
    print("Finished counting i without breaking.")

# While loop with a continue and an else
j = 0
while j < 5:
    j += 1
    if j == 2:
        print("Skipping j=2")
        continue
    print(f"j = {j}")
else:
    print("Finished counting j without breaking.")

# While loop with a nested for loop and a break
k = 0
while k < 3:
    print(f"Outer loop k={k}")
    for l in range(2):
        print(f"  Inner loop l={l}")
        if l == 1:
            print("  Breaking inner loop at l=1")
            break
    k += 1

# While loop with a nested while loop and a continue
m = 0
while m < 3:
    print(f"Outer loop m={m}")
    n = 0
    while n < 2:
        n += 1
        if n == 1:
            print("  Skipping n=1")
            continue
        print(f"  Inner loop n={n}")
    m += 1


# While loop with a nested for loop and an else
p = 0
while p < 2:
    print(f"Outer loop p={p}")
    for q in range(2):
        print(f"  Inner loop q={q}")
    else:
        print("  Finished inner loop without breaking.")
    p += 1

# While loop with a nested while loop and an else
r = 0
while r < 2:
    print(f"Outer loop r={r}")
    s = 0
    while s < 2:
        print(f"  Inner loop s={s}")
        s += 1
    else:
        print("  Finished inner loop without breaking.")
    r += 1

