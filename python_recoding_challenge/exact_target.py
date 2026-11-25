# Write a recursive function can_sum(nums, target, i=0) that returns True if any combination of numbers in nums adds up exactly to target. Otherwise, return False. Each element can either be included in the combination or excluded from it. Each element can only be used once

# Examples
# Input:   nums = [2, 4, 6, 10], target = 16
# Output:  True
# Explanation: 2 + 4 + 10 = 16.

# Input:   nums = [3, 5, 7], target = 12
# Output:  True

# Explanation: 5 + 7 = 12.
# Input:   nums = [-3, 4, 5], target = 3
# Output:  False

# Explanation: no combination of -3, 4 and 5 adds up to 3. The possible totals are -3, 4, 5, 1, 2, 9 and 6.
# Hints
# At every position, choose to include the current number or exclude it.
# Recursively explore both possibilities.
# Return True if either recursive path produces the target.
# Use the index parameter i to track your current position.
# Because negative numbers are allowed, do not stop merely because the remaining target is negative or positive.
# Constraints
# Zero for or while loops.
# Do not use sum().
# Do not use slicing such as nums[1:].
# Track your position using the index parameter i.
# Each element can only be selected once.
# Support both positive and negative integers.
# Do not hardcode the answers.
# What this tests: Recursive branching, include/exclude decisions, backtracking, index management, Boolean logic, and handling positive and negative integers.

   

def can_sum(nums, target, i=0):
    if i == len(nums):
        # print(i, len(nums))
        return target == 0
    
    inc = can_sum(nums, target - nums[i], i + 1)
    
    exc = can_sum(nums, target, i + 1)
    
    return inc or exc


# print(can_sum([3, 5, 8], 12))