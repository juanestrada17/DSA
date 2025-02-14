# The sliding window technique is an efficient way to solve problems 
# involving contiguous subarrays or substrings by maintaining a 
# "window" that expands or contracts dynamically while processing the input.


# Given an array and an integer k, find the maximum sum of any contiguous subarray of size k 

def max_sum_subarray(arr, k):
    
    # We compute the first k -> 3 elements sum
    # From 0 - 2 -> or [0] to [k-1]
    window_sum = sum(arr[:k])  # Initial window sum
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        # We remove the first element from the current window sum 
        # arr[i - k] removes in the first iteration is [0 - 0] effectively removing the first element
        window_sum += arr[i] - arr[i - k]  
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# Example
arr = [2, 1, 5, 1, 3, 2]
k = 3

print(max_sum_subarray(arr, k))  # Output: 9 (5 + 1 + 3)



# These tips might be helpful for sliding window problems:

# Remember that you usually declare two pointers initialized to 0 and need two loops

# You need an outer for loop to increment right pointer at each iteration.

# You need an inner while loop to increment the left pointer whenever the window/subarray is invalid.

# Algorithm template 

def sliding_window(nums, k):
    left = 0  # Left boundary of the window
    window_sum = 0  # To track sum/count/other metrics
    result = 0  # Store the final result

    for right in range(len(nums)):  # Expand the window
        # Include nums[right] in the window
        window_sum += nums[right]

        # (For fixed-size window) Ensure the window size is exactly k
        if right - left + 1 == k:
            # Process result (e.g., max/min/sum/average)
            result = max(result, window_sum)  # Example operation
            # Shrink the window by removing leftmost element
            window_sum -= nums[left]
            left += 1

        # (For variable-size window) Adjust left pointer dynamically
        while condition_not_met(window_sum):  # Define your condition
            window_sum -= nums[left]
            left += 1

        # You can update `result` here if needed

    return result
