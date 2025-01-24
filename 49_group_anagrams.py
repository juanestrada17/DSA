from collections import Counter, defaultdict
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

strs =  ["", "", "eat", "tea", ""]
res = []
sortedStrs = {}
for i in strs:
    # cur_sorted_str = "".join(sorted(i))
    cur_sorted_str = tuple(sorted(i))

    if(cur_sorted_str not in sortedStrs):
        sortedStrs[cur_sorted_str] = [i] 
    else:
        sortedStrs[cur_sorted_str].append(i)

for i in sortedStrs:
    res.append(sortedStrs[i])
    
# print(res)

# Second approach - unicode a-z -> 26 characters 

res = defaultdict(list)

for s in strs:
    count = [0] * 26 # a ... z

    for c in s:
        # current acsii value of c 
        # gets the index in the array and += 1 to it 
        # ex 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0 this is eat / we make it the key
        count[ord(c) - ord("a")] += 1 
            

    res[tuple(count)].append(s)
print(res.values())