# Problem
# A robot stands in the top-left square of a grid with rows rows and cols columns. It can only move one square right or one square down. Write a recursive function count_paths(rows, cols) that returns how many different routes the robot can take to reach the bottom-right square.
# Examples
# Input:   count_paths(2, 2)
# Output:  2

# Explanation: the two routes are right then down, and down then right.
# Input:   count_paths(3, 3)
# Output:  6

# Input:   count_paths(3, 2)
# Output:  3

# Input:   count_paths(1, 5)
# Output:  1

# Explanation: with only one row, the robot can only move right.
# Input:   count_paths(3, 7)
# Output:  28


def count_paths(rows, cols):
    if rows < 1 or cols < 1:
        return 0
    
    if rows == 1 or cols == 1:
        return 1
    
    return count_paths(rows - 1, cols) + count_paths(rows, cols - 1)


print(count_paths(2, 3))
