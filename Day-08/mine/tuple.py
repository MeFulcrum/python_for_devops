
my_tuple = (1, 2, 'apple', 'banana')

print("Initial tuple:", my_tuple)
#output : Initial tuple: (1, 2, 'apple', 'banana')
print("Length of tuple:", len(my_tuple))
#output : Length of tuple: 4
print("Item at index 2:", my_tuple[2])
#output : Item at index 2: apple
print("Item at last index:", my_tuple[-1])
#output : Item at last index: banana
print("Item at second last index:", my_tuple[-2])
#output : Item at second last index: apple
print("Slicing tuple [1:3]:", my_tuple[1:3])
#output : Slicing tuple [1:3]: (2, 'apple')
print("Iterating over tuple:")
for item in my_tuple:
    print(" -", item)
#output : 
# Iterating over tuple:
#  - 1
#  - 2
#  - apple
#  - banana

print("Reversed tuple:", tuple(reversed(my_tuple)))
#output : Reversed tuple: ('banana', 'apple', 2, 1)

if 'apple' in my_tuple:
    print("'apple' is in the tuple")
else:
    print("'apple' is not in the tuple")
#output : 'apple' is in the tuple
print("Tuple after converting to list and back:")
temp_list = list(my_tuple)
#output : temp_list = [1, 2, 'apple', 'banana']
temp_list.append('cherry')
#output : temp_list = [1, 2, 'apple', 'banana', 'cherry']
my_tuple = tuple(temp_list)
#output : my_tuple = (1, 2, 'apple', 'banana', 'cherry')

print("Final tuple:", my_tuple)
#output : Final tuple: (1, 2, 'apple', 'banana', 'cherry')

new_tuple = (3, 4, 5)
combined_tuple = my_tuple + new_tuple
print("Combined tuple:", combined_tuple)
#output : Combined tuple: (1, 2, 'apple', 'banana', 'cherry', 3, 4, 5)

def get_coordinates():
    return (40.7128, -74.0060)
lat, lon = get_coordinates()
print(f"Coordinates: Latitude = {lat}, Longitude = {lon}")
#output : Coordinates: Latitude = 40.7128, Longitude = -74.006


#Is Tuple ordered?
# Yes, tuples maintain the order of elements as they were defined.

#Are Tuples mutable?
# No, tuples are immutable; their elements cannot be changed after creation.

