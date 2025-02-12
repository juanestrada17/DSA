# nums array is sorted with distinct values 
# Objective = Return the index of the target in the nums array.
# Example = nums = [4,5,6,7,0,1,2] 
# target = 0 

def search_rotated_arr(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if target == nums[mid]:
            return mid
        
        if nums[left] <= nums[mid]:
            if target < nums[left] and target < nums[mid]:
                left = mid + 1
            elif target > nums[left] and target > nums[mid]:
                left = mid + 1
            else:
                right = mid 
        elif nums[left] >= nums[mid]:
            if target < nums[left] and target < nums[mid]:
                left = mid + 1
            elif target < nums[left] and target > nums[mid]:
                left = mid + 1
            else:
                right = mid
        
        

nums = [1,2]
target = 2
print(search_rotated_arr(nums, target))

# Simpler solution
# def search_rotated_arr(nums, target):
#     left, right = 0, len(nums) - 1
    
#     while left <= right:
#         mid = left + (right - left) // 2
        
#         if nums[mid] == target:
#             return mid
        
#         if nums[left] <= nums[mid]:  # Left half is sorted
#             if nums[left] <= target < nums[mid]:
#                 right = mid - 1
#             else:
#                 left = mid + 1
#         else:  # Right half is sorted
#             if nums[mid] < target <= nums[right]:
#                 left = mid + 1
#             else:
#                 right = mid - 1
                
#     return -1  # Target not found


 


    
