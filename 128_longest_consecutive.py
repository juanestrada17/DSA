# Given an unsorted array of integers nums, 
# return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

 
# Second apprach 
nums = [100,4,200,1,3,2]
dict = {key: 0 for key in nums}

for i in nums:
    if((i-1) not in dict):    
        starting_point = i
        dict[i] += 1
        while(starting_point + 1 in dict):
            dict[i] += 1
            starting_point += 1

print(max(dict.values()))


# Initial approach -> Works but performs poorly when array 
# is too long and it's descending
# for i in nums:
#     if(i in dict):
#         increasing_value = i
#         decreasing_value = i  
#         dict[i] += 1
#         while(increasing_value + 1 in dict):
#             dict[i] += 1
#             increasing_value += 1
#         while(decreasing_value - 1 in dict):
#             dict[i] += 1
#             decreasing_value -= 1
# print(max(dict.values()))

# Neetcode hashset solution
numSet = set(nums)
longest = 0 

for n in nums:
    # Means it's the starting point
    if (n-1) not in numSet:
        length = 0
        while(n + length) in numSet:
            length += 1
        longest = max(length, longest)
print(longest)


# 4 -> not in dict, -1 + 1 not in dict 
# 4:1
# 5-> not in dict, -1 in dict 
# 5:2
# 1 -> not in dict, -1 + 1 not in dict 
# 1: 1
# 3 -> not in dict, +1 IN dict -> is another +1 in dict? 
# 3: 2 
# 2 -> not in dict, 
#     +1 In dict -> is another  + 1 in dict? yes 
#     -1 in dict -> is another  - 1 in dict? no 
    

