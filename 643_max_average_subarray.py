# Objective = Find maximum average from a contiguous subarray of len k 
# expect float 
# Approach =
# Fixed window of len 4 
# Vars -> max_average (response), current_average (each time we calculate average from a window)
# 

from typing import List


def findMaxAverage(self, nums: List[int], k: int) -> float:
    # Optimized approach 
    # Calculate the sum until k 
    current_sum = sum(nums[:k])
    # Calculate the average until that point 
    max_average = current_sum / k 

    # Initialize the iteration from k, since we already calculated the first k elements and their average
    for right in range(k, len(nums)):
        # Add new element to sum
        current_sum += nums[right]
        # remove left-most element from sum
        current_sum -= nums[right - k]
        # check if average is higher
        max_average = max(max_average, current_sum / k)

    return max_average

  
# Original - not optimized   
# # The response
# max_average = float('-inf')
# # the current sum of elements in the current window
# current_sum = 0
# # The start point of the window 
# left = 0

# for right in range(len(nums)):
#     current_sum += nums[right]
#     window_size = (right - left) + 1

#     if window_size >= k:
#         # calculate the max average of current window
#         max_average = max(max_average, current_sum / k)
#         # Remove left from the sum 
#         current_sum -= nums[left]
#         # Reduce window size because it exceeds or equals k 
#         left += 1 

# return max_average



