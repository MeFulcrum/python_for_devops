
check1 = ["jack", "black", "choco", "loco"]

print("type of check1", type(check1))

check2 = {"jack", "black", "choco", "loco"}
print("type opf check2" , type(check2))

set1 = check2
print("type of set1", type(set1))

set1.add("moco")
print("set1 after adding moco", set1)

#set1.pop()
#print("set1 after popping loco", set1)
#Removes and returns an arbitrary element from the set. Raises KeyError if the set is empty.

set1.remove("jack")
print("set1 after removing jack", set1)

set2 = {"jack", "black", "choco", "loco" ,"moco", "boco", "floco"}
print("set 1 is :", set1)
print("set 2 is :", set2)

print("difference between set1 and set2", set1.difference(set2))
print("Meaning of difference: elements in set1 that are not in set2")

print("difference between set2 and set1", set2.difference(set1))
print("Meaning of difference: elements in set2 that are not in set1")

print("intersection of set1 and set2", set1.intersection(set2))
print("Meaning of intersection: elements that are in both set1 and set2")

print("intersection of set2 and set1", set2.intersection(set1))
print("Meaning of intersection: elements that are in both set2 and set1")

print("union of set1 and set2", set1.union(set2))
print("Meaning of union: all unique elements from both set1 and set2")

print("union of set2 and set1", set2.union(set1))
print("Meaning of union: all unique elements from both set2 and set1")

print("is set1 a subset of set2?", set1.issubset(set2))
print("is set2 a subset of set1?", set2.issubset(set1))

