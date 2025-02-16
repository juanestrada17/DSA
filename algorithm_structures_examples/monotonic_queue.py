# Maintains elements in an increasing or decreasing order
# Efficient to add and remove elements to the beginning in O(1)

# Example in decreasing order ->
# 1|1|1|1|1  New element = 4
# We pop all elements at the top that are less that 4 

# Then we add the 4, which is in this case the highest
# The deque becomes -> |4| 


# [8, 7, 6, 9]
# 8 New element  = 7 
# Since it's not less that 8, we add it to the deque
 