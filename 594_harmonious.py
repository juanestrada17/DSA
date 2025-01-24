# We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

# Given an integer array nums, return the length of its longest harmonious 
# subsequence
#  among all its possible subsequences.

 

# Example 1:
# Input: nums = [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation:
# The longest harmonious subsequence is [3,2,2,2,3].
nums = [-1, 0, -1, 1, -1, 0, 1]
nums.sort()
# 1,2,2,2,3,3,5,7
#step one
left, right = 0, 1 # 1,2
currentLongest = 0
while right < len(nums):
    if(nums[left] == nums[right]):
        right += 1
    else:
        minimum = min(nums[left], nums[right])
        maximum = max(nums[left], nums[right])
        if(maximum - minimum == 1):
            currentLongest = max(currentLongest, right - left + 1) 
            right += 1 
        else: 
            left += 1
print(currentLongest)

# class Solution:
#     def findLHS(self, nums: List[int]) -> int:
#         freq,ans=Counter(nums),0
#         for x in freq: 
#             if x+1 in freq: ans=max(ans, freq[x]+freq[x+1])
#         return ans 

# Approach
# The key is an element of nums, and the value is its frequency.
# So for every x in the hashmap, we check if x + 1 exists or not.
# If it does, we calculate the length of such a sequence, which is simply the sum of their frequencies.