# Given an integer array nums, return all the triplets 
# [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

nums = [-1,0,1,2,-1,-4]
# Sort the array 
nums.sort()
res = []

for i in range(len(nums)):
    
    # Handle duplicates, if we already iterated through -1 combinations we don't need to do it again
    if i > 0 and nums[i] == nums[i-1]:
        continue 
    # next element after current
    j = i + 1 
    # the last element, since it's sorted it's the highest
    k = len(nums) - 1
    
    while j < k:
        # add all numbers 
        current_sum = nums[i] + nums[j] + nums[k]
        
        # if the current sum is higher than 0 it means we have to reduce the highest
        if(current_sum > 0): 
            k -= 1
        # if the current sum is less than 0 it means we have to increase j to a higher element
        elif(current_sum < 0):
            j += 1
        # we reach 0, so we append to the array
        else:
            new_el = [nums[i], nums[j], nums[k]]
            # We check if there are duplicates in the element is already inside to handle duplicates
            
            res.append([nums[i], nums[j], nums[k]])
            # We increment j, to find another element that meets the 0 condition with current i and to exit the while loop
            j += 1
            
            # Handles duplicates when multiple j [-2, 0, 0, 0, 1, 2]
            while nums[j] == nums[j - 1] and j < k:
                j+= 1
        

print(res)
            
            
