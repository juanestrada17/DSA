# Each row is sorted
# next row's first int is always higher than every 
# element in previous rows 

# Objective = Find the target in the matrix  
# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# target = 3 
matrix = [[1]]
target = 0

def search_matrix(matrix, target):
    # Flatten the array using a list comprehension
    flattened_matrix = [num for subArr in matrix for num in subArr]

    # Perform binary search over it, since it's sorted
    left, right= 0, len(flattened_matrix)

    while left < right: 
        mid = left + (right - left) // 2
        
        if flattened_matrix[mid] == target: 
            return mid 
        elif flattened_matrix[mid] > target: 
            right = mid
        else:
            left = mid + 1
print(search_matrix(matrix, target))            

# Another option is to perform binary search using the sub arrays
# We target the mid element of the matrix, then perform binary search there if the target is less than the max in this sub arr
# Basically, binary search over binary search 