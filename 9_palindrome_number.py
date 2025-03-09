# Objective = Return true if it's palindrome, else false 
# Sting approach -> Slower - working with strings is slow
x = 121
def palindrome_number(x):
    xStr = str(x)
    left, right = 0, len(xStr) -1 

    while left < right: 
        if xStr[left] == xStr[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

print(palindrome_number(x))


# Remainder approach
def isPalindrome(x):
    # If it's a negative number it's never a palindrome 
    if x < 0:
        return False
    
    reverse = 0 
    xcopy = x 
    
    # x % 10 extracts the last digit
    # (reverse * 10) + (x % 10) appends the last digit to the correct position
    # x //=10 removes the last digit 
    # ex -> 123 -> reverse = 0
    # First iteration - > reverse = (0 * 10) + 3 = 3
    # Second iteration -> reverse = (3 * 10) + (x % 10) = 32
    # Third iteration -> reverse = (32 * 10) + (x % 10) = 321
    while x > 0: 
        reverse = (reverse * 10) + (x % 10)
        x //= 10
    return reverse == xcopy

