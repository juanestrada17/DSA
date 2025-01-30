# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all 
# non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

s = "A man, a plan, a canal: Panama"

def valid_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1    
        while left < right and not s[right].isalnum():
            right -= 1
        
        if(s[left].lower() != s[right].lower()):
            return False
        
        left += 1
        right -= 1
    return True

print(valid_palindrome(s))

# Approach using python slicing
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         clean = [c for c in s.lower() if c.isalnum()]
#         return clean == clean[::-1]