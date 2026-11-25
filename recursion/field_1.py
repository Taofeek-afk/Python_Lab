def reverse(string: str) -> str:
    if len(string) == 0:
        return ""
    
    # Take the last character + reverse the rest of the string
    return string[-1] + reverse(string[:-1])

# print(reverse("hello"))  # Output: olleh


def reverse_2(string: str):
    if len(string) == 0:
        return ""
    
    return string[len(string)-1] + reverse_2(string[:len(string)-1])


# print(reverse_2("apple"))


# Lesson 6: counting occurrences in a string, 
# which introduces a very useful recursive pattern.


def count_occurence(string: str, char: str) -> int:
    # Base case: an empty string contains 0 occurrences
    if len(string) == 0:
        return 0
    
    # Check if the last character matches
    match = 1 if string[-1] == char else 0
    
    # Return match (1 or 0) + result of the rest of the string
    return match + count_occurence(string[:-1], char)


# print(count_occurence("banana", "a"))  # Output: 3
# print(count_occurence("hello", "l"))   # Output: 2


def count_occurence_2(string: str, char: str):
    if len(string) == 0:
        return 0
    
    index = len(string) - 1
    
    match = 1 if string[index] == char else 0
    
    return match + count_occurence_2(string[:len(string)-1], char)


# print(count_occurence_2("banana", "a"))



def count_occurence_3(string: str, char: str):
    if len(string) == 0:
        return 0
    
    match = 1 if string[0] == char else 0
    
    return match + count_occurence_3(string[1:], char)


# print(count_occurence_3("banana", "a"))


def sum_list(arr: list[int]) -> int:
    if len(arr) == 0:
        return 0
    
    return arr[0] + sum_list(arr[1:])


# print(sum_list([2, 3, 4, 5]))
# print(sum_list([20, 15, 10, 5]))


def power(base: int, exponent: int) -> int:
    if exponent == 0:
        return 1

    return base * power(base, exponent - 1)


# print(power(2, 4))


def mystery(n: int) -> None:
    if n == 0:
        return

    print(n)
    mystery(n - 1)
    print(n)


# mystery(3)



# Problem:

# Given an array and a target, determine whether the target exists.

# Example:

# [4, 7, 2, 9, 5]

# Search for:

# 9 → True

# Search for:

# 8 → False

def find_target(arr: list[int], target: int):
    if len(arr) == 0:
        return False
    
    if arr[0] == target:
        return True
    
    # print(arr)
    
    return find_target(arr[1:], target)


# print(find_target([4, 7, 2, 9, 5], 8))


def find_target_2(arr: list[int], 
    target: int,
    index: int = 0) -> bool:
    
    if index >= len(arr):  # Defensive programming.
        return False
    
    if arr[index] == target:
        return True
    
    return find_target_2(arr, target, index + 1)


# print(find_target_2([4, 7, 2, 9, 5], 8))


def find_index(arr: list, target: int, index = 0):
    if index >= len(arr):
        return -1
    
    if arr[index] == target:
        return f"Target {arr[index]} found at index {index}"
    
    return find_index(arr, target, index + 1)


# print(find_index([4, 7, 2, 9, 5], 9))
# print(find_index([4, 7, 2, 9, 5], 8))


def sum_range(start: int, end: int) -> int:
    if start > end:
        return 0
    
    return start + sum_range(start + 1, end)


# print(sum_range(3, 3))

def binary_search_slice(arr: list[int], target: int):
    if not arr:
        return "Target not found"
    
    mid = len(arr) // 2
    
    if arr[mid] == target:
        return True
    elif arr[mid] > target:
        return binary_search_slice(arr[:mid], target)
    else:
        return binary_search_slice(arr[mid+1:], target)


# print(binary_search_slice([1, 2, 3, 4, 5], 9))


def binary_search(
    arr: list[str],
    target: str,
    left: int,
    right: int,
) -> int:
    # Base case: search space is empty
    if left > right:
        return -1

    mid = (left + right) // 2

    # Target found
    if arr[mid] == target:
        return mid

    # Search left half
    if target < arr[mid]:
        return binary_search(arr, target, left, mid - 1)

    # Search right half
    return binary_search(arr, target, mid + 1, right)


arr = ["a", "b", "c", "d", "e"]

print(binary_search(arr, "c", 0, len(arr) - 1))  # 5
print(binary_search(arr, "b", 0, len(arr) - 1))   # 2
print(binary_search(arr, "f", 0, len(arr) - 1))  # -1
