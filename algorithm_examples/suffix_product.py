arr = [1,2,3,4]

suffix_product = [1] * len(arr)
suffix_product[-1] = arr[-1]

for i in range(len(arr) -2, -1, -1):
    suffix_product[i] = suffix_product[i + 1] * arr[i]

print(suffix_product)

# If we want not inclusive
noni_suffix_product = [1] * len(arr)

for i in range(len(arr) -2, -1, -1):
    noni_suffix_product[i] = noni_suffix_product[i+1] * arr[i + 1]

print(noni_suffix_product)