nums = [1,2,3,4,5]
k = 2
# Objetive = Split nums into k non-empty subarrays 
# step 1 -> after dividing 2 subarrays, calculate the longest sum between the two
# step 2 -> Find another combination -> calculate the longest sum between two
# Step 3 -> If it's smaller than current longest, set it 
# Expected output = 18 

def split_array_lar_sum(nums, k):
    # 18
    def is_possible_largest(large_num):
        k_nums = 1
        curr_sum = 0 
        for num in nums:
            curr_sum += num
            if curr_sum > large_num:
                k_nums += 1
                curr_sum = num
        if k_nums <= k: 
            return True
        else: 
            return False
            

    # case when input [1,7] -> min will never be the answer
    # Max can be the min answer 
    # Max element is the sum of all elements, when k = 1 
    left, right = max(nums), sum(nums)
    
    while left < right:
        mid = left + (right - left) // 2
        
        if is_possible_largest(mid):
            right = mid 
        else:
            left = mid + 1
    return left
print(split_array_lar_sum(nums, k))
    # pass it an output within the range and determine if it is a valid output or not







# [7]
# [2,5,10,8] = 25

# [7,2]
# [5,10,8] = 23 

# [7,2,5] =14 
# [10,8] = 18 

# [7,2,5,10] = 24
# [8]
