# Objective: Find the duplicate number
# Important array contains n + 1 elements, these elements are always between [1,n]
# Example -> element at index 4 point to index 2 
# nums = [1,3,4,2,2]
from typing import List


nums = [1,3,4,2,1]

# The len of the array is n + 1
# Every value in the array is between 1 and n.
# Simplified =  There's n different values, but n + 1 positions
# Values can be considered as pointers:
# For example |1|3|4|2|2 -> 1 points at position 1(val 3) -> 3 points at position 3(val 2)
# we NEVER point at index 0, it's never in the cycle 
# 0 -> 3 -> 2 -><- 4. When there are multiple pointers pointing at node 2, we know its a dupliclate

# STEPS= 
# 1. Identify the beginning of a cycle - Floyd's algorithm (slow/fast pointers)
# 2. With Floyd's algorithm determine the intersection of the two pointers
# 3. Start two slow pointers. 1 from start and another one from the intersection 
# 4. When the new slow and the first intersection point intersect, that's the response 

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0 
        
        while True:
            slow = nums[slow]
            # Advances twice as fast
            fast = nums[nums[fast]]
            # If both of them meet, we stop the while loop 
            if slow == fast:
                break 
        # We know this is where they intersect
        # When  two different indices point to the same number we found the
        # Cycle entrance and duplicate creates a loop
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

# Hare and tortoise algorithm
# The duplicate creates a cycle, when we move two pointers from the start of the cycle to the start of the array, the distance
# will give us the duplicate. The distance from the start of the array to the cycle start is the same as the distance from the
# meeting point back to the cycle start

