# You are given an integer array height of length n. There are n vertical lines drawn such 
# that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

height = [9,8,7,6,5,4,3,2,1]
# height = [1,2,3,4,5,6,7,8,9]
# index 0 / 5 
# 9 / 5 

# Width = higher index - smaller index
# Height = min(height2, height1)
# Area = width * height

left, right = 0, len(height) - 1
max_amount = 0

while left < right:
    width = right - left 
    h = min(height[right], height[left])
    
    area = width * h
    if area > max_amount:
        max_amount = area 
    
    if height[right] > height[left]:
        left += 1
    else:
        right -= 1
    
    
print(max_amount)

