def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        return "error" #checks if num and divisor are numeric, returns error if either are not
    
    return num % divisor == 0 #modulo returns the remainder after division, when the remainder is 0, the numbers are divisible
    
# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3

check_divisibility (10, 2)
check_divisibility (7, 3)
