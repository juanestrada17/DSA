# m are bouquets
# k are adjacent flowers from garden to make m 
# garden - n flowers 
# Elements in the array represent the day a flower blooms.
# Each time a flower blooms it can be used for a bouquet 

# Objective = return the minimum number of days you need to wait
# to make m bouquets from the garden, else -1 

# Example :
# bloomDay = [1,10,3,10,2], m = 1, k = 1
# Output is = 3 (3 days)
# Why? Day 1, element[0] of the array blooms and forms a bouquet
# Day 2 element[-1] of the array blooms and forms a bouquet
# Day 3 element[2] of the array blooms and forms a bouquet | Since we get to the goal -> m = 3 We have the solution

# Approach
# Determine the min and max of the binary search array 
# Min = minimum element from the array -> We can complete a bouquet of 1 flower in 1 day 
# Max = max element of the array -> It can't ever take more than the max amount of days, when all flowers have bloomed we know are supposed to know our answer

# Edge case 
bloomDay = [1542,5142,4695,4385,2629,2492,933,1068,151,3960,3790,1196,3842,5147,5526,5528,2259,1708,2714,5462,3016,3262,1175,4348,4826,80,789,5285,3855,3455,3480,4277,648,1748,625,4256,3931,4938,4553,2129,4480,824,3048,2383,3036,2192,2156,7,438,5258,2430,2459,3769,1694,1687,5130,70,3219,4140,2341,1159,3952,4934,4335,2786,3124,5344,803,4586,1000,2821,4769,629,4673,3920,3437,4533,2984,3576,5364,1255,1876,2309,5619,2402,1978,4127,1668,147,4139,292,1499,1786,2435,1988,146,500,3377,3789,1301,1193,1686,3501,3895,1321,1587,4263,593,1580,3652,1638,4905,1927,567,2797,2082,1349,4158,679,4944,4638,4770,3458,2117,2620,938,4121,2374,1478,5269,5548,5125,5237,1693,2188,690,4640,827,2721,2329,430,4423,5510,2312,2493,4884,223,1904,4660,5124,2851,5227,4160,694,5660,5571,834,1704,4550,988,573,3373,5419,311,4280,399,5319,4723,5467,1155,4267,303,4233,770,3087,3306,1042,4192,3736,893,5087,1903,3650,393,5304,2767,3562,5501,4789,1863,1653,2528,5521,3802,3925,2718,5402,2642,304,4171,4356,5486,1426,4526,4541,4310,2160,4542,2850,2396,1612,4780,3921,5219,2585,4027,1861,3799,101,1434,996,203,1216,1654,4382,3791,3417,1912,5337,814,352,3892,3851,3432,2400]
m = 49 # 49 bouquets
k = 4 # 4 flowers

def min_num_bouquets(bloomDay, m, k):
    n = len(bloomDay)
    # if we don't have enough flowers we do an early return 
    if m * k > n:
        return -1
    
    def form_bouquets(expected_days):
        bouquets = 0
        flowers = 0  
        
        for day in bloomDay:
            # If the day is less that the possible day we add flowers each iteration
            if day <= expected_days: 
                flowers += 1
                # Once the flowers reach the amount to form a bouquet we add to the bouquet and reset flowers
                if flowers == k: 
                    bouquets += 1
                    flowers = 0
            else:
                # If the day is bigger than the specified reset (this handles adjacent flowers only)
                flowers = 0
        # Handles case when we have the required bouquets or MORE than them
        return bouquets >= m
    
    left, right = min(bloomDay), max(bloomDay)    
    while left < right:
        mid = left + (right - left) // 2

        # if the current mid passed is correct, we reset right
        if form_bouquets(mid):
            right = mid 
        else:
        # else we reset left 
            left = mid + 1
    # since we are finding the minimum we return the left element with our bin search 
    return left

print(min_num_bouquets(bloomDay, m, k))

    


