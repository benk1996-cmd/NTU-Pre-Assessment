def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    #checks the data type of x and y and returns -1 if either are not numeric
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1 
    
    #swaps the values of x and y
    x = x + y
    y = x - y
    x = x - y
    
    print(x, y)




# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17

swap ("Apple",10)
swap (9,17)
