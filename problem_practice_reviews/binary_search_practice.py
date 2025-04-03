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

def shipPacksDays(weights, days):
    # Objective: determine the capacity at which the weights can be shipped withing days 
    # weights = [1,2,3,4,5,6,7,8,9,10] / days = 5 / output = 15 
    # Helper function to determine if a capacity works for the amount of days give 
    def possibleCapacity(capacity): 
        # get a hold of the days passed 
        daysPassed = 1 
        # get a hold of the sum within days 
        currentDaySum = 0
        for weight in weights: 
            
            # if the sum exceeds the capacity we pass a day and reset current day sum 
            if currentDaySum + weight > capacity: 
                daysPassed += 1
                currentDaySum = weight
            
            # add weight
            else:
                currentDaySum += weight
        # true if the daysPassed are lower or equal to the days 
        return daysPassed <= days
    # Min and max 
    minCapacity = max(weights) # The min capacity can't ever be lower than the max element in the weights. Ex: [1,10], can't ever be 1 because it can't ship 10
    maxCapacity = sum(weights) # if all of them are shipped in the same day, that would be the case with the max capacity 
    left, right = minCapacity, maxCapacity
    # binary search 
    while left < right:
        capacity = left + (right - left) // 2
        
        # If it's a possible capacity we search a lower possible capacity 
        if possibleCapacity(capacity): 
            right = capacity
        else: 
            left = capacity + 1
    # always return the min
    return left
    
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5 


def minBouquetDays(bloomDay, m, k):
    # Objective = make m bouquets with k adjacent flowers 
    # example = [7,7,7,7,12,7,7], m = 2, k = 3. Make two with 3 adjacent flowers
    
    # If the amount of flowers surpases the bloom day flowers 
    if m * k > len(bloomDay):
        return - 1  
    
    # We pass it a day, we try to form m bouquets with the given day
    def formBouquets(day):
        addedFlower = 0
        bucketSum = 0 
        for bDay in bloomDay:
            # this means it has bloomed 
            if bDay <= day:
                # add a flower to a bouquet
                addedFlower += 1
                # if we reach k, it means the bouquet is complete
                if addedFlower == k:
                    bucketSum += 1
                    addedFlower = 0      
            else: 
                # If there are no adjacent flowers we reset it 
                addedFlower = 0 
        return bucketSum >= m
                 
        
    # Determine min - max 
    left, right = min(bloomDay), max(bloomDay)
    while left < right: 
        mid = left + (right - left) // 2 
        
        if formBouquets(mid):
            right = mid
        else:
            left = mid + 1 
    return left
bloomDay = [1,10,3,10, 2]
m = 3 
k = 1

def kthSmallestInTable(m, n, k):
    # Objective = Return the kth smallest element in the table m * n.
    # ex: 3 * 3 ->  k = 5 -> [1,2,2,3,3,4,6,6,9] -> the fifth smallest num is 3 
    def isPossible(target):
        count = 0 
        
        # row 
        for num in range(1, m + 1):
            # find how many values satisfy it being lower than target
            rowLessThanTarget = min(target // num, n)
            count += rowLessThanTarget
        
        return count >= k
    
    
    # min, max 
    left, right = 1, n * m
    
    while left < right: 
        mid = left + (right - left) // 2

        if isPossible(mid):
            right = mid 
        else:
            left = mid + 1 
    return left 
        
    
m = 3
n = 3 
k = 5 

def searchInRotatedArray(nums, target):
    # Objective = The array is sorted, but there might be a pivot. Example = [4,5,6,7,0,1,2], target = 0. Perform bisearch with o(log n)
    # We need to check if either the left side or the right side is sorted 
    
    left, right = 0, len(nums) - 1
    
    while left < right: 
        mid = left + (right - left) // 2 
        
        if nums[mid] == target:
            return nums[mid]
        
        # This means the array is sorted to the left 
        elif nums[left] <= nums[mid]:
            # if the target is within left and mid, we search more elements on the left side
            if nums[left] <= target < nums[mid]:
                right = mid 
            else: 
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    