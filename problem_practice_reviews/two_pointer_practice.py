# Two Pointers algorithms work by adding a pointer at the start and another at the end 

def validPalindrome(s):
    # Reads same forward and backward
    left, right = 0, len(s) - 1
    
    while left < right: 
        # Case when empty space 
        while left < right and not s[left].isalnum():
            # Skip empty spaces to left
            left += 1 
        while left < right and not s[right].isalnum():
            right -= 1 
        
        # If the two letters are different then its not a palindrome 
        if s[left].lower() != s[right].lower():
            return False

        left += 1 
        right -= 1 
    return True        
s = "A man, a plan, a canal: Panama"


def twoSomeSorted(numbers, target):
    # Return index + 1 of the sum of two numbers that add up to the target 
    left, right = 0, len(numbers) - 1
    
    
    while left < right: 
        currSum = numbers[left] + numbers[right]

        if currSum == target:
            return [left + 1, right + 1]
        elif currSum  > target:
            right -= 1
        else:
            left += 1 
            
numbers = [2,7,11,15]
target = 9 # target = 22  if target 9 reduce right, if target 22 increase left 

# Objective is to find all triplets that add up to 0 in an array 
def TreeSum(nums):
    # We need to sort this, this will allow a similar solution to the twoSomeSorted problem 
    nums.sort()
    res = []
    # We have three pointers 
    # Pointer 1 is the current element with multiple combinations 
    for i in range(len(nums) - 1):
        # We need to check for duplicates, let's say nums[0] and nums[1] are both 1, we need to prevent this 
        # We continue the loop if this is the case 
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # Pointer 2 is initially the element after pointer 1 
        j = i + 1 
        # Pointer 3 is the last element of the array  
        k = len(nums) - 1 

        # Evaluate if their sum is 0         
        while j < k:  
            # Check if their sum is 0
            total = nums[i] + nums[j] + nums[k]

            if total == 0:
                # Add them to the array 
                res.append([nums[i], nums[j], nums[k]])
                # Increment j to see if there are other combinations  
                j += 1
            
            # If the total is higher than 0 
            elif total > 0: 
                k -= 1
            # if the total is less than 0  
            else: 
                j += 1 
                # We need to check for duplicates also with j similar to the code above 
                while nums[j] == nums[j - 1] and j < k: 
                    j += 1
    return res 

# Width = higher index - smaller index
# Height = min(height2, height1)
# Area = width * height
def maxArea(height):
    # Return maximum amount of water a container can store
    left, right = 0, len(height) - 1
    maxAmount = 0 
    while left < right:
        width = right - left 
        height = min(height[right], height[left])
        area = width * height
        
        maxAmount  = max(maxAmount , area)
        
        if height[right] > height[left]:
            left += 1 
        else:
            right -= 1 
    return maxAmount 
        

height = [1,8,6,2,5,4,8,3,7]
  
def trap(height):
    # Objective = Return the amount of water it can trap between elevations
    trappedWater = 0
    left, right = 0, len(height) - 1
    # Left and right boundaries 
    maxLeft, maxRight = height[left], height[right]
    while left < right: 
        # Calculate how much water is trapped to the left 
        if maxLeft < maxRight: 
            # Example -> maxLeft is 1 and current left or height[left] is 0. Then trapped water becomes 1 
            trappedWater += maxLeft - height[left]
            left += 1
            # We check if the current left is exceeds the previous max 
            maxLeft = max(maxLeft, height[left])
        else:
            # When the maxLeft >= maxRight  
            trappedWater += maxRight - height[right]
            right -= 1
            maxRight = max(maxRight, height[right])
    return trappedWater