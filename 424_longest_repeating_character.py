s = "BBBABAB"
k = 1

# 1. If array == k -> Then res == k
# 2. Res is never higher than the len of s 
# 3. We can use a hashmap to store the frequency of each letter

counter = {}
maxFreq = 0 
left = 0 
maxLen = 0
for right in range(len(s)):
    # set it to 0 if it doesn't exist, else set it to it's value + 1
    counter[s[right]] = counter.get(s[right], 0) + 1
    # check if it's the current longest substring
    maxFreq = max(maxFreq, counter[s[right]])
    
    
    # We remove the most frequent letter from the substring. If that amount exceeds k it means 
    # we have violated the condition of more than k flips    
    while (right - left + 1) - maxFreq > k:
        # If that's the case we have to reduce the window by deleting left letter from dict
        counter[s[left]] -= 1
        # we also need look to the right of the array 
        left += 1 
    # We calculate maxLen by comparing the current max len with the distance between left and right after the
    # changes
    maxLen = max(maxLen, right - left + 1)
    
