# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]
# nums = [2,15,11,7]
# target = 9

# Possible approach -> we substract the target and check if the result is in nums
nums = [11,2,1,7]
target = 9
# arr = []
# leftI = 0
# rightI = 0
# numberToFind = 0
# for i in range(len(nums)):
#     if(nums[i] == numberToFind):
#         rightI = i
#     else:
#         if(target - nums[i] in nums):
#             leftI = i
#             numberToFind = target - nums[i]

# print([leftI, rightI])

# Dicionary approach -> O(n)
dict = {}
for i, val in enumerate(nums):
    diff = target - val
    
    if(diff in dict):
        print([i, dict[diff]])
    dict[val] = i
    
   
    