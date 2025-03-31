# find mid, determine if target is higher or lower than mid
# list is usually sorted 

def binarySearch(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right: 
        # mid = (left + right) // 2
        # to prevent integer overflow in languages like java or c, we use the 
        mid = left + (right - left) // 2
        
        if nums[mid] == target: 
            return nums[mid]
        
        elif nums[mid] > target: 
            # search on the left side of mid 
            right = mid - 1 
        
        else: 
            # serach on the right side since target is bigger than mid 
            left = mid + 1
    # Or return - 1
    return None

# Brute force O(m * n) 
def search2DMatrix(matrix, target):
    # Find the target in a matrix where each element is sorted 
    # Each row start is higher than previous row 
    flattenedMatrix = [i for el in matrix for i in el]
    
    # flatMatrix = []
    # for el in matrix:
    #     for i in el:
    #         flatMatrix.append(i)
             
    res = binarySearch(flattenedMatrix, target)
    return True if res else False

def searchMatrix(matrix, target): 
    left, right = 0, len(matrix) - 1 
    while left <= right: 
        mid = left + (right - left) // 2 
        
        # This means that the target is within the current mid array. So we stop searching for a mid with the answer 
        if matrix[mid][0] <= target and matrix[mid][-1] >= target:
            break 
        
        # If the first element is higher than the target, then it must be in a left array 
        elif matrix[mid][0] > target:
            right = mid - 1 
        
        # if the last element is lower than the target, then it must be to the right 
        else:
            left = mid + 1  
        
    # Early return when the target is not within any of the rows 
    if left > right: 
        return False 
    
    row = matrix[mid]
    # the current mid is the array containing the target, so we perform bisect over it 
    res = binarySearch(row, target)
    
    # bool(res) works too
    return True if res else False
     
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3 

# print(searchMatrix(matrix, target))  
# print(search2DMatrix(matrix, target))


# Problems to find min using binary search 

def minEatingSpeed(piles, h):
    # Objective = 
    # minimum amount of bananas that koko eats so that she'll eat all of them in h hours 
    
    # The range of the binary search will be between 1 and the max amount of bananas
    left, right = 1, max(piles)
    
    while left < right:
        # Mid represents the eating speed or amount of bananas per hour. 
        mid = left + ( right - left) // 2 
        
        # Current sum is resetted to 0 / amount of hours taken to eat bananas in all piles
        currentSum = 0
        # Loop through the piles to calculate the currentSum 
        # This can be transformed into a helper function 
        for pile in piles: 
            currentSum += (pile + mid - 1) // mid
        # If the current sum is less than h try searching 
        if currentSum <= h: 
            right = mid
        else: 
        # Koko needs to eat more bananas -> case when total hours spent are 8 and h = 5
            left = mid + 1
    return left 

# option with helper function /  better
def minEatingSpeedH(piles, h):
    def isPossibleSpeed(piles, eatingSpeed):
        currentSum = 0 
        for pile in piles: 
            currentSum += (pile + eatingSpeed - 1) // eatingSpeed
        return currentSum <= h # we can finishin within h hours 
    
    left, right = 1, max(piles)
    while left < right: 
        # ceiling division, round down to nearest int 
        mid = left + (right - left) //2
        
        if isPossibleSpeed(mid): 
            # It's a valid response, we search if there's another that's less 
            right = mid 
        else: 
            left = mid + 1
    return left      

    

piles = [3,6,7,11]
h = 8 
# Expected 4 -> eats 4 hour 1 
# eats 4 hour 2 -> 2 remain
# eats 2 hour 3 -> 0 remain 
# eats 4 hour 4 -> 3 remain
# eats 3 hour 5 -> 0 remain 
# eats 4 hour 6 -> 7 remain
# eats 4 hour 7 -> 3 remain
# eats 3 hour 8 -> 0 remain. All piles eaten 

piles = [30, 11, 23, 4, 20]
h = 5 
# expected = 30 