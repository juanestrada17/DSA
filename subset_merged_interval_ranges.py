# a = [1,2,3]

# b = [2,5,5]

# c = a + b 
# c.sort()
# print(c)

ranges = [[1,5], [3,8], [10, 15], [13,14], [20, 100]]
# ran = [[208, 416], [305, 1287], [100, 405]]
# We sort the ranges by their [0] element, so we guarantee they are contiguous
ranges.sort()

merged = []

# start is each array's [0] and end is [1]
for start, end in ranges:
    # if the current range is not in merged OR the end of the previous range is smaller than the start of next
    # when merged[-1][1] it means the two arrays don't have anything in common
    if not merged or merged[-1][1] < start:
        # We add them 
        merged.append([start, end])
    else:
        # We merge the two ranges with same elements -> Example ->
        # merged = [[1,5]] -> Since the next element is [3,8] and 5 is higher than 3
        # we set that range to either the end of [3,8] or the end of [1,5]
        # since 8 > 5 we set it to 8
        merged[-1][1] = max(merged[-1][1], end)

# len of merged
k = len(merged)
# We use modulo 
MOD = 10 ** 9 + 7
result = (pow(2, k, MOD) - 2) % MOD

# print(result)
# test = [[1,5], [3,8], [10, 15], [13,14], [20, 100]]
