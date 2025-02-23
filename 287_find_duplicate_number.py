# Objective: Find the duplicate number
# Important array contains n + 1 elements, these elements are always between [1,n]
# Example -> element at index 4 point to index 2 
# nums = [1,3,4,2,2]
nums = [1,3,4,2,1]

# Hare and tortoise algorithm
# The duplicate creates a cycle, when we move two pointers from the start of the cycle to the start of the array, the distance
# will give us the duplicate. The distance from the start of the array to the cycle start is the same as the distance from the
# meeting point back to the cycle start


# [1,3,4,2,2]
# 1 -> 3 - 4 
# 3 -> 4 - 2
# 4 -> 2 - 2

# [3,1,3,4,2]
# 3 -> 1 - 3
# 1 -> 3 - 4 
# 3 -> 4 - 2 


