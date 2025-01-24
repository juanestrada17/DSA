# Requirement = In Binary search the list must be sorted 
# Steps 
# 1. Find mid 
# 2. Check if the target is the same as the mid
# 3. Check if the target is less or higher than mid 
# 4. if it is same, we return value. Else we search in the left or right part

sorted_list = [1, 3, 5, 7, 9, 11, 13]
target = 1

left, right = 0, len(sorted_list) - 1

while left <= right:
    # We find the middle index of the array 
    mid = (left + right) // 2
    
    # If we found the value, we print its value
    if(sorted_list[mid] == target):
        print(mid)
        break
    elif(sorted_list[mid] < target):
        left = mid + 1 # we search in the right part, so we "remove" the left
    else: 
        right = mid - 1 # we search in the left part, so we "remove" the right


