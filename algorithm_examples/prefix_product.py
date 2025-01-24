arr = [1,2,3,4]

prefix_product = [1] * len(arr)

for i in range(len(arr)):
    if i == 0:
        prefix_product[i] = arr[i]  # First element is just the array's first element
    else:
        prefix_product[i] = prefix_product[i - 1] * arr[i]    
print(prefix_product)

# If we want not inclusive
noni_prefix_product = [1] * len(arr)

for i in range(1, len(arr)):
    noni_prefix_product[i] = noni_prefix_product[i-1] * arr[i -1]

print(noni_prefix_product)