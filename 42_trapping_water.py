# Given n non-negative integers representing an elevation 
# map where the width of each bar is 1, compute how much water it can trap after raining.

height = [4,2,0,3,2,5]
left, right = 0, len(height) - 1
max_left, max_right = height[left], height[right] 
current_water = 0

while left < right:
    # Starting point -> either starts left or right, where the max is lower
    if max_left < max_right:
        # We calculate the trapped water by substracting the highest minus the current, 
        # this gives us the amount of blocks with trapped water
        current_water += max_left - height[left]
        left += 1
        # We increment the max when it's higher
        if height[left] > max_left:
            max_left = height[left]
    else:
        # If the max_left is higher than the right_max
        current_water += max_right - height[right]
        right -= 1 
        if height[right] > max_right:
            max_right = height[right]
        
print(current_water)

# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array 
# [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.


# [3,2,1,2,1]
# output 1

# [4,2,0,3,2,5]
# output 9 






