my_list = [1, 2, 3, 'apple', 'banana']
mnum = [4, 35, 6, 27, 18]
print("Initial list:", my_list)
my_list.append('cherry')
print("After appending 'cherry':", my_list)
my_list.remove(2)
my_list.remove(my_list[3])  # removes 'banana'
my_list.append(10)
my_list.append(5)
my_list.append("jackfruit")
my_list.append('appa')
print("After removing 2:", my_list)
#This does not sort number as expected but do sort STRINGS and places numbers before strings 
my_list.sort(key=str) #this works because we are sorting based on string representation and 10 can be converted to string   
print("After sorting:", my_list)
#print("Simple Sorting", my_list.sort(key=int)) # GIves error becuase of different data types apple cannot be considerred as integer so it gives error
print("Number list before sorting:", mnum)
mnum.sort()
print("Number list after sorting:", mnum)
print("Length of list:", len(my_list))
print("Item at index 2:", my_list[2])
print("Item at last index:", my_list[-1])
print("Item at second last index:", my_list[-2])
print("Simple list before slicing:", my_list)
print("Slicing list [1:4]:", my_list[1:4])
print("Iterating over list:")
for item in my_list:
    print(" -", item)
print("Reversed list:", list(reversed(my_list)))

print("reveversed is without list", list(reversed(my_list)))


if "banana" in my_list:
    print("'banana' is in the list")
else:
    print("'banana' is not in the list")

print("List after clearing all items.")
my_list.clear()
print("Final list:", my_list)
# """List operations examples (Day-08 notes)
# Demonstrates basic list operations: append, remove, sort, length, indexing, slicing, iteration, and clearing.
# Run: python list.py
# """