# s = "abcabcbb"
s = "pwwkewp"
# s = "bbbb"
# s= "abcabcbb"
# s = "dvdf"
# s = " "
# Objective = Find len of longest substring without
# repeating characters




def lengthOfLongestSubstring(s: str) -> int:
    char_index = {}  # Stores character and its last index
    max_length = 0
    left = 0

    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left:
            # let's say it's pwwkewp
            # pw -> left is 0, right is 1
            # pww -> left BECOMES 2, right is 2 -> we update index of w to be 2
            # pw/ wke -> left is 2, right is 4
            # pw/wkew -> left BECOMES 3, right is 5 -> We update index of w to be 5
            left = char_index[s[right]] + 1  # Move left to avoid repeating character
        
        char_index[s[right]] = right  # Update the index of the current character
        max_length = max(max_length, right - left + 1)

    return max_length

print(lengthOfLongestSubstring(s))

# Initial solution
# def is_valid_substring(s):
#     n = len(s)
#     setN = len(set(s))
    
#     return n == setN

# left, right = 0, 1 
# count = 0 
# max_count = 0
# while right <= len(s):
#     if is_valid_substring(s[left:right]):
#         max_count = max(max_count, len(s[left:right]))
#     else:
#         left += 1
#     right += 1
# print(max_count)    

    





# max_len = 0
# for index, letter in enumerate(s):
#     print(s[index:])
#     if is_valid_substring(s[index:]):
#         max_len = max(max_len, len(s[index:]))
    
# print(max_len)

    
    


# Example 
# s = "abcabcbb"
# 3 

# nums_count = []
# count = 0
# max_count = 0
# right = 0  
# for letter in s:
#     if letter not in nums_count:
#         nums_count.append(letter)
#         count += 1
#         max_count = max(max_count, count)
#     else:
#         max_count = max(max_count, count)
#         left = 0 
#         if nums_count[left] == letter:
#             nums_count.pop(left)
#         else:
#             while nums_count[left] != letter:
#                 nums_count.pop(left)
#         nums_count.append(letter)
#         count = len(nums_count)
# print(max_count)
# when there's a repeated element 
# calculate len, append rep element, slice from prev - current



# d -> v (count 2)
# since d is in left part 
# v -> d -> f (count 3)
# -----------------------
# a -> b -> c (count 3)
# since a is in left part 
# b -> c -> a 
# c -> a -> b
# a -> b -> c 
# b -> c 
# b 
# ------------------------
# abcb
# a -> b -> c 
# b -> c 
# c -> b




# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 