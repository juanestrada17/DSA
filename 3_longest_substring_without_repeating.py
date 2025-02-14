s = "abcabcbb"
s = "pwwkewp"
s = "bbbb"
s= "abcabcbb"
s = "dvdf"
s = " "
# Objective = Find len of longest substring without
# repeating characters

# Dynamic window 
# left is the first element, right is the first element also 
# We can check the frequency of each letter, if the letter exceeds 1, then shrink 

# Example 
# left, right =  0, 0 / {d: 1} -> max is 1
# left, right = 0, 1 / {d: 1, v: 1} -> max is 2
# left, right = 0, 2 / {d:2, v:1} -> Since d violates the condition we shrink window
# left, right = 1, 2 / {d:1, v: 1} -> max is 2 
# left, right = 1, 3 / {d:1, v:1, f:1} -> max is 3, res is 3  

# A set would be more suitable, rather than a hashmap 
left = 0 
letter_freq = {}
longest_sub = 0 
for Rindex, right in enumerate(s):
    
    while right in letter_freq: 
        del letter_freq[s[left]]
        left += 1
    
    window_size = (Rindex - left) + 1
    longest_sub = max(longest_sub, window_size)
    letter_freq[right] = 1
print(longest_sub)

# s = "pwwkewp"
# left, right = 0, 0 / {p:1} -> max is 1
# left, right = 0, 1 / {p:1, w:1}
# left, right = 0, 2 / {p:1, w:2} -> violates
# left, right = 1, 2 / {w:2} -> violates
# left, right = 2, 2 / {w:1} 
# left, right = 2, 3 / {w:1, k:1}
# left, right = 2, 4 / {w:1, k:1, e:1}
# left, right = 2, 5 / {w:2, k:1, e:1} -> violates
# left, right = 3, 5 / {w:1, k:1, e:1}
# left, right = 3, 6 / {w:1, k:1, e:1, p:1} -> max is 4 

# An approach with a set 
def lengthOfLongestSubstring(s: str) -> int:
    left = 0
    char_set = set()
    longest_sub = 0

    for right in range(len(s)):
        # Shrink the window if the character is already in the set
        while s[right] in char_set:
            char_set.remove(s[left])  # Remove leftmost character
            left += 1  # Move left pointer forward
        
        char_set.add(s[right])  # Add new character to the set
        longest_sub = max(longest_sub, right - left + 1)  # Update max length
    
    return longest_sub



# def lengthOfLongestSubstring(s: str) -> int:
#     char_index = {}  # Stores character and its last index
#     max_length = 0
#     left = 0

#     for right in range(len(s)):
#         if s[right] in char_index and char_index[s[right]] >= left:
#             # let's say it's pwwkewp
#             # pw -> left is 0, right is 1
#             # pww -> left BECOMES 2, right is 2 -> we update index of w to be 2
#             # pw/ wke -> left is 2, right is 4
#             # pw/wkew -> left BECOMES 3, right is 5 -> We update index of w to be 5
#             left = char_index[s[right]] + 1  # Move left to avoid repeating character
        
#         char_index[s[right]] = right  # Update the index of the current character
#         max_length = max(max_length, right - left + 1)

#     return max_length

# print(lengthOfLongestSubstring(s))
