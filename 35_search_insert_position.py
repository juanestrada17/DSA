# Output = 2 
nums = [1,3,5,6]
target = 7

def search_insert_position(nums, target):
    left, right = 0, len(nums) - 1 
    
    while left <= right: 
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid 
        elif nums[mid] < target:
            left = mid + 1
        else: 
            right = mid - 1
    return left

# [1,3,5,6]
# [5,6]
# [6]

print(search_insert_position(nums, target))
# Objective = 
# return the index if the target is found
# if not, return where it would be inserted considering it's sorted


