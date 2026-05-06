def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    i = 0
    while i < len(lst):          #iterates through each value in the list
        if lst[i] < 0:           #checks if value is less than 0
            return lst[i]        #exits loop and returns value if less than 0
        i += 1                   #if not, loop moves to next value in list
    
    return "No negatives"        #if list is exhausted without finding any negative values, return text "No negatives"

# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]

find_first_negative ([3, 5, -1, 7, -2, 8])

find_first_negative ([2, 10, 7, 0])
