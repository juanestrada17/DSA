# Objective -> store timestamps and retrieve keys values at a certain timestamp

# set("foo", "bar", 1)  // Store "bar" for key "foo" at timestamp 1
# get("foo", 1)  // Should return "bar" (since timestamp matches)
# get("foo", 3)  // Should return "bar" (since 1 is the closest timestamp <= 3)
# set("foo", "baz", 5)  // Store "baz" for key "foo" at timestamp 5
# get("foo", 4)  // Should return "bar" (since 1 is the closest timestamp <= 4)
# get("foo", 5)  // Should return "baz" (since timestamp matches)
# get("foo", 6)  // Should return "baz" (since 5 is the closest timestamp <= 6)
dict = {}

dict["foo"] = [(1, "baz")]
dict["foo"].append((2, "baz2"))
dict["foo"].append((3, "baz3"))
dict["foo"].append((10, "baz10"))
dict["foo"].append((5, "baz5"))

print(dict)
target = 11
# Objective -> Find the element or the closest min element to target 
test = [(1),(2),(3),(4),(10)]
left = 0
right = len(test) - 1

res = 0 
while left < right:
    mid = left + (right - left) // 2
    
    if test[mid] == target:
        res = test[mid]
        break
    
    if target > test[mid] and target < test[mid + 1]:
        res = test[mid]
        break
    
    if test[mid]> target:
        right = mid
    else: 
        left = mid + 1
if res:
    print(res)
else:
    print(test[left])
        

# Final solution 
# class TimeMap:

#     def __init__(self):
#         self.timeMap = {}        

#     def set(self, key: str, value: str, timestamp: int) -> None:
        
#         #Structure looks similar to this 
#         # {'foo': [(1, 'baz'), (2, 'baz2'), (3, 'baz3'), (10, 'baz10'), (5, 'baz5')]}
#         if key not in self.timeMap:
#             self.timeMap[key] = [(timestamp, value)]
#         else:
#             self.timeMap[key].append((timestamp, value))

#     def get(self, key: str, timestamp: int) -> str:

#         if key not in self.timeMap:
#             return ""
        
#         targetArr = self.timeMap[key]
#         left, right = 0, len(targetArr) 
#         res = ""


#         while left < right:
#             mid = left + (right - left) // 2

#             if targetArr[mid][0] == timestamp:
#                 return targetArr[mid][1]

#             # update the element that's less than timestamp
#             elif targetArr[mid][0] < timestamp:
#                 res = targetArr[mid][1]
#                 left = mid + 1       

#             else:
#                 right = mid
#         return res

# # Your TimeMap object will be instantiated and called as such:
# # obj = TimeMap()
# # obj.set(key,value,timestamp)
# # param_2 = obj.get(key,timestamp)