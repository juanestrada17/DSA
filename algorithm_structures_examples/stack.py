# Linear data structure that follows the LIFO principle. Last in first out, last element added
# is also the first one to be removed

# Push, pop -> add, remove
# Peek, top -> View top element 

# In python we can use deque from collections to achieve this. deque is optimized for  LIFO and FIFO
# Principles
s = 'StrToReverse'
stack = []
for st in s:
    stack.append(st)

reversed_str = ''
while stack:
    reversed_str += stack.pop()
print(reversed_str)