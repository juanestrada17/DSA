# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 
s = "]"
# stack = []
# dict = {')': '(', '}': '{', ']':'['}

# for char in s: 
#     if(char not in dict):
#         stack.append(char)
#     elif(char in dict):
#         last_element = stack.pop()
#         if(last_element != dict[char]):
#             print("Not Valid")

# if(stack):
#     print("Not Valid")        
# else:
#     print("valid")


# First approach - refined
dict = {'(': ')', '[': ']', '{':'}'}
stack = []


for el in s:
    if el in dict:
        stack.append(el)
    
    elif(stack):
        last_element = stack.pop()
        if(el != dict[last_element]):
            print("Not Valid")
    else:
        print("not Valid")

if(stack):
    print("Not valid")

