# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes 
# all the following ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a 
# function to find the first bad version. You should minimize the number of calls to the API.

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # Since it's a range we start at 1 and end at n [1,2,3,4,5]
        # the bad versions are 4-> 5 
        left, right = 1, n

        while left < right:
            mid = left + (right-left) // 2

            # example -> first mid is 3 -> it's not a bad version so we do left = mid + 1
            # [4,5] -> new mid is 4, it's a bad version we do right = mid
            # [4] -> the loop ends and we return the minimum value, remaining value 4. Which is left 
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left 
    
