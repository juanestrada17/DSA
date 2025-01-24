# longest nice substring. A nice substring is a letter that appears both cap and lower

s = "cChhHzxXxdt"
# expected result is -> "cChH"
left, right = 0,0 
current_len = 0 
final_substring = ""
max_len = 0
arr = []
while right < len(s):
    if(s[left].lower() == s[right].lower()):
        final_substring += s[right]
        right += 1
        # current_len += 1 
        
    elif(s[left].lower() != s[right].lower()):
        if(s[left].upper() in final_substring and s[left].lower() in final_substring):
            left = right 
        else: 
            final_substring = final_substring.replace(s[left], "")
            # current_len -= 1
            arr.append(final_substring)
            # max_len = max(max_len, current_len)
            # current_len = 0
            final_substring = ""
            left += 1
            right = left

print(arr)


# substring = "c" left 0 / right 0 
# next one is c -> it's the same letter add it 
# substring = "cc" left 0 / right 1 
# next one is C -> it's the same letter add it 
# substring = "ccC" left 0 / right 2 
# next one is h -> it's different, we check if the current substring contains a cap letter 
#     if it does -> continue -> left = right + 1 / right + 1  
#     substring = "ccCh"
#     if it doesn't -> stop   
# next one is H -> it's the same letter add it 
# substring ="ccChH"
# next one is z -> it's different, we check if the current substring contains left.upper() and left.lower()
# substring = "ccChHz"
# next one is X -> it's different, we check if the current substrinc contains...
# it doesn't, so we break and remove the latest element from substring

# cccCzZzttRx 












# Works with same letter
# s = "dDzeE"
# dict = {}
# left = 0 
# hasCaps = False
# hasLows = False
# start = 0
# end = 0 
# current_len = 0 

# for right in range(len(s)):
    
#     if(s[left].lower() != s[right].lower()):
#         if(hasCaps and hasLows):
            
#             if((right - left) > current_len):
#                 current_len = max(current_len, right - left)
#                 start = left
#                 end = right
        
#         hasCaps = False
#         hasLows = False
#         left = right
        
#     if(s[left].lower() == s[right].lower()):
#         if(s[left].isupper() or s[right].isupper()):
#             hasCaps = True
        
#         if(s[left].islower() or s[right].islower()):
#             hasLows = True
            
#         if(hasCaps and hasLows and right == len(s) - 1):
#             if((right - left) + 1 > current_len):
#                 current_len = max(current_len, (right - left) + 1)
#                 start = left
#                 end = right + 1

# print(s[start:end])
# print(current_len)

# thought process
# aAa -> 3 
# count = 0 
# left == index 0 
# right == index 0 
# hasCaps = False
# we check if left is same as right ->
#     index 0 is Y -> they are the same and it has caps so flag is set to True
#     increment right plus 1 

# left == 0 
# right == 1 
# hasCaps = True 
# we check if left is same as right ->
#     left -> Y and right -> a -> they are different so we set flag to False  
#             we set the count to the len of it -> 1 - 0 

# increment left == 1
# right  == 2 
# hasCaps = false
# left = a - right = A -> They are the same and one of them is caps, set flag to True
#     increase right + 1

# left == 1
# right == 3
# left = A - right = a -> they are the same 

# 1 - 4
# left = a - right = y -> different, set flag to false 
#         set count to len max(current count, new count)
#         left = right
#         right + 1 = 5 
        



# all letters, even if not together
# s = "YazaAay"
# dict = {}
# left = 0
# right = 1 
# longest = 0 
# sortS = sorted(s)
# for i in range(len(sortS)):
#     if(sortS[i].isupper()):
#         dict[sortS[i]] = 1
#     elif(sortS[i].upper() in dict):
#         dict[sortS[i].upper()] += 1

# print(dict)
