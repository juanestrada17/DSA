# Given an array of integers temperatures represents the daily temperatures, return an array answer such
# that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]

temperatures = [73,74,75,71,69,72,76,73]
# stack -> It contains the indexes
stack = []
res = [0] * len(temperatures)

for i in range(len(temperatures)):
    # if stack is not empty and the current temperature is higher than previous temperature
    while stack and temperatures[i] > temperatures[stack[-1]]:
        # Pops the previous element's index from the array, and sets it to be the current iteration index - previous index
        # Example = stack = [0], temperatures[stack[-1]] = 30 > 40 
        # we pop 0 and, add the amount in the res 0 position 
        idx = stack.pop()
        # Calculates the position of the element in the stack index array
        res[idx] = i - idx
    # appends the index of the temperature to the stack 
    stack.append(i)
print(res)
