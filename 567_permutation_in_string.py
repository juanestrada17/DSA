from collections import Counter

s1 = "ab"
s2 = "eidbaooo"

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Frequency of each element in each string
        s1_freq = Counter(s1)
        s2_freq = Counter()

        left = 0
        for right in range(len(s2)):
            # Add element and increase frequency + 1 in second dictionary
            s2_freq[s2[right]] += 1

            # If the window exceeds k -> len(s1) 
            if right - left + 1 > len(s1):
                # Remove left element from dict and from window
                s2_freq[s2[left]] -= 1
                # If the element gets to 0, we delete it
                if s2_freq[s2[left]] == 0:
                    del s2_freq[s2[left]]
                left += 1
            # When both dicts are equal we return True 
            if s1_freq == s2_freq:
                return True
        return False
        

# def solution(s1, s2):
#     def matches_string(s, k, s1_freq):
#         temp_freq = s1_freq.copy()
#         counter = 0 
#         if s[0] not in temp_freq :
#             return False 
#         for letter in s:
#             if letter in temp_freq :
#                 if temp_freq[letter] <= 0: 
#                     return False
#                 else:
#                     temp_freq[letter] -= 1
#                     counter += 1
#             else:
#                 return False
#         if counter == k:
#             return True
#         else:
#             return False

#     # window is 3 -> eib -> If left character is not in s1_freq, move window 
#     # window is 3 -> iba -> If left character is not in s1_freq, move window 
#     # window is 3 -> baa -> 

#     # for x in baa: 
#     #     if freq[x] is 0 break return false
#     #     if x in freq and freq[x] not 0 reduce it's frequency 
#     s1_freq = {}
#     k = len(s1)
#     for letter in s1:
#         if letter not in s1_freq:
#             s1_freq[letter] = 1
#         else:
#             s1_freq[letter] += 1

#     left = 0 
#     for right in range(k, len(s2) + 1):
#         current_string = s2[left:right]
#         if matches_string(current_string, k, s1_freq):
#             return True
#         else: 
#             left += 1
#     return False
# print(solution(s1, s2))

             
    


    
        




# Objective = return true if a permutation of s1 is in s2 
# Permutations are differen ordered combinations of a string

