import copy 
# Reference assignment
# This is not a copy, it's another reference to a var. Another "name" for array 
# example = 
# array2 = array
# When you modify something in array2 it's also affected in reference 1

array = [1,2,3,[4]]
array2 = array 
print(array)
print(array2)
print("After modifying one of the two, by setting first element to 0 and appending 4 to nested list")
array2[0] = 100
array2[3].append(5)
print(array)
print(array2)
print("-----------------------------------")
# Shallow copies
# Outer list is copied, references stay the same 
print("Shallow copies: After modifying one of the two, by setting first element to 0 and appending 4 to nested list")
array = [1,2,3,[4]]
array3 = copy.copy(array)
array3[0]  = 100
array3[3].append(5)
print(array)
print(array3)
print("-----------------------------------")
# Deep Copy
# Everything is copied, including nested structures such as nested arrays. One is completely independent
# From the other. 
array = [1, 2, 3, [4]]
print("Deep copies: After modifying one of the two, by setting first element to 0 and appending 4 to nested list")

array4 = copy.deepcopy(array)
array4[0] = 100
array4[3].append(5) 
print(array)
print(array4)

# NOTE -> For sets deep copy behaves the same as shallow copy, since they don't have duplicates. 