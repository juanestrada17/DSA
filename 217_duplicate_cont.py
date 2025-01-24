# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

nums = [4,2,3,1]

# Initial approach 
# Make it a set, if the len is different than the original array then return true, else false. 
# len(nums) != len(set(nums))

# Second approach
# we sort the array and check if element at index left and right match, if not increment left
nums.sort()
left =  0
res = False
for right in range(1, len(nums)):
    if(nums[left] == nums[right]):
        res = True
        break
    else:
        left += 1
        
print(res)

# Third approach using hash set
# Adds the number to a set, if while looping an existing element exists break. 
# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         seen = set()
#         for num in nums:
#             if num in seen:
#                 return True
#             seen.add(num)
#         return False
    
