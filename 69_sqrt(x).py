x = 8 # integer

# Objective = return the square root of x rounded down to the nearest 
# closes non-negative int
# 1 * 1 = 1 
# 2 * 2 = 4 
# 3 * 3 = 9 
# 4 * 4 = 16 

def squart(x):
    if x < 2:
        return x 
    
    left, right = 1, x // 2
    while left < right:
        mid = left + (right - left) // 2    
        square = mid * mid 
        if square == x:
            return mid
        if square > x:
            right = mid - 1
        else: 
            left = mid + 1
    return right

print(squart(x))


# def mySqrt(x: int) -> int:
#     left, right = 0, x
#     while left < right:
#         mid = left + (right - left) // 2
#         if mid * mid <= x:
#             left = mid + 1
#         else:
#             right = mid
#     return left - 1