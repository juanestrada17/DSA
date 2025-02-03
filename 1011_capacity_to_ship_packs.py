# days    = 5 
# weights = [1,2,3,4,5,6,7,8,9,10]
# output= 15 
# Can't load weight over max capacity 
# # Objective = least weight capacity that leads to all packs
# delivered within the days specified 
# Example -> if the max weight is 15 -> 
# we can load 
# 1,2,3,4,5 -> 15 day 1
# 6,7 -> 13 day 1 
# 8
# 9 
# 10 

from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def det_valid_cap(capacity) -> bool:
            curr_sum = 0
            days_spent = 1
            for w in weights:
                # If the sum of the current elements is higher than the capacity it means all possible elements were shipped
                # we spend a day
                if curr_sum + w > capacity:
                    days_spent += 1
                    curr_sum = w
                # If it's less or equal than capacity we keep adding elements
                else:
                    curr_sum += w
            # if the days spend don't exceed the expected days, we return true
            return True if days_spent <= days else False

        # capacity can't ever be lower than the highest element / weight
        min_capacity = max(weights) 
        # Capacity can't ever be higher than the sum of all weights, because it would make it
        # impossible to ship all weights in 1 day. 
        max_capacity = sum(weights) 
        left, right = min_capacity, max_capacity

        while left < right:
            mid = left + (right - left) // 2
            # If the capacity is valid, we search with a lower capacity 
            if det_valid_cap(mid):
                right = mid
            else: 
                left = mid + 1
        return left
        

# If a combination is possible with current mid we adjust
# the right to search for a lower 

# if a combination is not possible with current mid, 
# we adjust the left 

