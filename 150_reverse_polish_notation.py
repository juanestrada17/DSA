# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.
 
 
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
stack = []
operators = {"+", "*", "/", "-"}
for token in tokens: 
    if(token in operators):
        second_element = int(stack.pop())
        first_element = int(stack.pop())
        if(token == "+"):
            sum_res = first_element + second_element
            stack.append(sum_res)
        elif(token == "*"):
            prod_res = first_element * second_element
            stack.append(prod_res)
        elif(token == "/"):
            div_res = int(first_element / second_element)
            stack.append(div_res)
        else:
            sub_res = first_element - second_element
            stack.append(sub_res)
    else:
        stack.append(token)

print(stack[0])
# Example 1:

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:


# Input: tokens = 
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# Example 3:


# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
 
 