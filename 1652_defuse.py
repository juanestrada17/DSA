# Modulo

[5,7,1,4]






# You have a bomb to defuse, and your time is running out! Your informer will provide you with a
# circular array code of length of n and a key k.

# To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.

# If k > 0, replace the ith number with the sum of the next k numbers.
# If k < 0, replace the ith number with the sum of the previous k numbers.
# If k == 0, replace the ith number with 0.
# As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

# Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!

# Input: code = [2,4,9,3], k = -2
# 4,9,3,2
# Output: [12,5,6,13]
# Explanation: The decrypted code is [3+9, 2+3, 4+2, 9+4]. Notice that the numbers wrap around again.
# If k is negative, the sum is of the previous numbers.
 

code = [3, 8, 2, 5, 6, 1, 4]
code_len = len(code)
k = 4
res = []

total = 29 
if(k == 0):
    res = [0] * (len(code)) 
    
left = code_len - 1
total_sum = sum(code)

for right in range(code_len):
    if(k > 0):
        res.append(total_sum - code[right])
    if(k < 0):
        next_element = 0 if right + 1 > code_len - 1 else right + 1
        res.append(total_sum - code[right] - code[next_element])
        
print(res)




# Example 2:



# Input: code = [1,2,3,4], k = 0
# Output: [0,0,0,0]
# Explanation: When k is zero, the numbers are replaced by 0. 
# Example 3:

