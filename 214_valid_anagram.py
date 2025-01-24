from collections import Counter
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly once. Listen / Silent 
s = "anagram"
t = "nagaram"

# First approach -> Sort both strings and check if the sorted result is the same
# print(sorted(t) == sorted(s))

# hash approach 
# Approach 2 
sElements = {}
tElements = {}
for el in s:
    if(el not in sElements):
        sElements[el] = 1
    else:
        sElements[el] = sElements[el] + 1


for el in t:
    if(el not in tElements):
        tElements[el] = 1
    else:
        tElements[el] = tElements[el] + 1


# print(sElements == tElements)

# Counter Approach 
sCount  = Counter(s)
tCount  = Counter(t)
print(sCount == tCount)