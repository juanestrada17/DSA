# original array = [1,2,3,4,5]
# rotated array = [3,4,5,1,2]

# Test cases
# nums = [5,1,2,3,4]
nums = [1,2]
# nums = [2,1]
# nums = [4,5,6,0,1,2,3]
# nums = [3,4,5,1,2]


def find_min(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        
        # If the mid is higher than the right, it means the result must be at the right
        if nums[mid] > nums[right]:
            left = mid + 1
        # If the mid is lower than the right, it means the result must be mid or left of mid 
        else:
            right = mid 
    # Return minimum number 
    return nums[left]
