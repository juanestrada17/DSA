# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas.
# The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she 
# chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, 
# she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return
# Return the minimum integer k such that she can eat all the bananas within h hours.
# Objective: how many bananas can eat per iteration, so that she eats all piles before h 

# len(piles ) < h. [1,2,3,4,5,6] -> h = 5

piles = [30,11, 23, 4, 20]
h = 5

# The range-> min is 1, and not 0 because if it were 0 it would mean Koko is not eating any bananas from a pile in an hour
left, right = 1, max(piles)
while left < right:
    mid = (left + right) // 2 
    
    current_sum = 0 
    for pile in piles: 
        # same as math.ceil(pile / mid)
        current_sum += (pile + mid - 1) // mid 
    
    if current_sum <= h:
        right = mid
    else:
        left = mid + 1
        
print(left)






# if it's lower than target h -> decrease the number in the range (change it to mid)
# if it's higher than target h > increase the number in the range  (change it to mid)
# print(count)


# Example 1:

# Input: piles = [3,6,7,11], h = 8
# Output: 4
# 4 bananas per hour 
# pile 1 -> 3 bananas 
# pile 2 -> 4 bananas  - 2 bananas
# plie 3 -> 4 bananas  - 3 bananas
# pile 4 -> 4 bananas  - 4 bananas - 3 bananas

# Example 2:

# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
# 30 -> 30 bananas
# 11 -> 30 bananas 
# 23 -> 30 bananas
# 4 -> 4 bananas
# 20 -> 30 bananas



# Example 3:

# Input: piles = [30,11,23,4,20], h = 6
# Output: 23