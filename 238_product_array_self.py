nums = [-1,1,0,-3,3]

# Calculate prefix product array - index not included
# 1,1,2,6 -> Expected result 
prefix_product = [1] * (len(nums))
for i in range(1, len(prefix_product)):
    prefix_product[i] = prefix_product[i - 1] * nums[i - 1]
    
# Calculate suffix product array - index included
# 24,12,4,1 -> Expected result 
suffix_product = [1] * (len(nums))

# -2 means it's not the final index, which always is 1.
# -1 because we need it to calculate when it's at index 0
# -1 because we start from end to start
for i in range(len(suffix_product) -2, -1, -1):
    suffix_product[i] = suffix_product[i + 1] * nums[i + 1] 

res = []
for i in range(0, len(prefix_product)):
    res.append(suffix_product[i] * prefix_product[i])

print(res)