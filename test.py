# a = 7 
# print(a.__str__())

# import datetime
# print(type(datetime.date(2012, 1,1) - datetime.date(2011, 1,1)))

# import itertools
# Counts from 5 - 10, then excludes multiples of five 
# res = [i for i in filter(lambda x:x % 5, itertools.islice(itertools.count(5), 10))]
# print(res)

import re 
text = "abc123def456ghi"
pattern = r"(?:abc)\d+"
matches = re.findall(pattern, text)
# print(matches)
print(10/0)

test = [3,3,3,3,3,5,1]

# str = "abc"

# test = sorted(str)
# res = ''.join(test)
# print(res)

sorted_nums = sorted(set(test), reverse= True)
res = []
for num in test: 
    if num in sorted_nums:
        res.append(sorted_nums.index(num) + 1)

print(res)