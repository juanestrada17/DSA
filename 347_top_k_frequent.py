# Given an integer array nums and an integer k, return the k most frequent elements. 
# You may return the answer in any order.

# Solution using sorts and hash maps, first approach
import heapq


nums = [2,1,3,2,1,1]
nSet = set(nums)
k = 2
count = {}

# Create a dictionary with the frequency of each item
for i in range(len(nums)):
    if(nums[i] not in count):
        count[nums[i]] = 1
    else: 
        count[nums[i]] += 1 

# sort the items descending 
# lambda specifies a custom function
# kv: kv[1] points to the values in the dictionary. if we did kv[0] it would point to the keys, sorting by keys
# This returns a list of tuples so it would be something like [(1,3), (2,2), (3,1)]
sorted_items = sorted(count.items(), key=lambda kv: kv[1], reverse=True)

# we loop through the elements and stop when the len of the response is k or higher
final_arr = []
for element, count in sorted_items:
    if(len(final_arr) < k):
        final_arr.append(element)

# print(final_arr)


# Bucket sort - approach  O(n)
# Bucket sort works 2 ways 
# 1. we check the max element[1,1,1,2,2,100] -> 
        # frequency 
        # elements 0|1|2|...|100
# 2. we check the frequency of each instead of the element
# frequency -> 0|1    |2  |3  |4|5|6
# values    ->  |[100]|[2]|[1]| | | | -> 100 once, 2 twice, 1 three tiems

count = {}
freq = [[] for i in range(len(nums) + 1)]

for num in nums:
    count[num] = 1 + count.get(num, 0)

for num, cnt in count.items():
    # example cnt = 1 and num = 3 
    freq[cnt].append(num)

res = []
# we do it descending, because we care about the highest elements 
for i in range(len(freq) - 1, 0, -1):
    for num in freq[i]:
        res.append(num)
        if len(res) == k:
            print(res)



# Third approach Neetcode - Heap 
count = {}
for num in nums: 
    count[num] = 1 + count.get(num, 0)

heap = []
for num in count.keys():
    heapq.heappush(heap, (count[num], num))
    if(len(heap) > k):
        heapq.heappop(heap)
res = []
for i in range(k):
    res.append(heapq.heappop(heap)[1])
# print(res)



