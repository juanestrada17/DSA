# m -> 3 
# n -> 3
# k -> 5

# m * n is the size of the matrix 

# Objective -> find kth smallest element 
# Smallest means we need to sort the matrix in ascending order 
# Smallest element will always be = 1 when k is 1
# Highest element will always be m * n. Or the array's last element 

# arr = [1,2,3,4,5,6,7,8,9,10]

# mid = left + (right - left) // 2
m = 3
n = 3
k = 5 
def calc_smallest_in_table(m, n, k):
    
    def possibleSmallest(mid):
        count = 0 
        # Returns the amount of elements before mid at each row
        for num in range(1, m + 1):
            # We use min, to limit the elements before mid to be the max size
            # of n 
            current_smallest = min(mid // num, n) 
            count += current_smallest    
        
        return count >= k
        
    left, right = 1, m * n
    
    while left < right:
        mid = left + (right - left) // 2
        
        if possibleSmallest(mid):
            right = mid
        else: 
            left = mid + 1
    return left

print(calc_smallest_in_table(m,n, k))




# 1, 2, 2, 3, 3, 4, 6, 6, 9




# Possible solution -> create matrix -> sort it -> use index 
