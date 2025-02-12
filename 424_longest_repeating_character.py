s = "BBBABAB"
k = 1

# 1. If array == k -> Then res == k
# 2. Res is never higher than the len of s 
# 3. We can use a hashmap to store the frequency of each letter

charCount = {}
maxFreq = 0
left = 0
maxLen = 0

for right in range(len(s)):
    # If it exists return it, else return 0 
    charCount[s[right]] = charCount.get(s[right], 0) + 1
    maxFreq = max(maxFreq, charCount[s[right]])
    
    # Right - left + 1 is the size of the window 
    # maxFreq is the current Longest substring
    # If at some point this is higher than k. Example in AABABBA K= 1. When {A=3, B=2} -> Max freq is 3, win size is 5 > k
    # This equation represents the number of replacement needed 
    while (right - left + 1) - maxFreq > k:
        charCount[s[left]] -= 1
        left +=1
        
    maxLen = max(maxLen, right - left + 1)
print(maxLen)
