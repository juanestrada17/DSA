arr = [1,2,3,4]

prefix_sum = [0] * len(arr)
prefix_sum[0] = arr[0]
for i in range(1, len(arr)):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i]

print(prefix_sum)
    