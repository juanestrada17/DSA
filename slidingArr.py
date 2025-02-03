def calcLen(nums, target):
    length = float('inf') 
    current_sum = 0 
    left, right = 0, 0 
    
    while right < len(nums):
        
        current_sum += nums[right]
        
        while(current_sum >= target):
            length = min(length, right - left + 1)
            current_sum -= nums[left]
            left += 1 
        right += 1 
    if(length == float('inf')):
        return 0
    return length


nums = [2,3,1,2,4,3]
target = 7