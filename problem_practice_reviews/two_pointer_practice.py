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
    
    currSum = numbers[left] + numbers[right]
    
    while left < right: 
        if currSum == target:
            return [left + 1, right + 1]
        if currSum  > target:
            right -= 1
        else:
            left += 1 
            
numbers = [2,7,11,15]
target = 9 # target = 22  if target 9 reduce right, if target 22 increase left 

def TreeSum(nums):
    # find triplets that have a sum of 0
    # We need to sort the numbers so that k will be the largest element and i will be the lowest 
    nums.sort()
    
    # i is the first element, base loop
    res = []
    for i in range(len(nums) - 1):
        
        # Check for dups 
        # check if element before current i is not the same 
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        j = i + 1 # element after current i 
        k = len(nums) - 1 # last element 
        
        # We need to add the tree element 
        while j < k:  
            total = nums[i] + nums[j] + nums[k]
            
            if total == 0: 
                res.append([nums[i], nums[j], nums[k]])
                j += 1 
            # If its higher than 0 it means we need to search in a lower element
            elif total > 0: 
                k -= 1 
            else:
                # total is less than 0, we need to search a higher element
                j += 1 
            # Check for j duplicates             
            if j < k and nums[j] != nums[j - 1]:
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