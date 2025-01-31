nums = [-1,0,3,5,9,12]
target = 9
left, right = 0, len(nums) - 1

while left <= right:
    mid = (left + right) // 2 
    
    if nums[mid] == target:
        print(mid)
        break
    
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

        
