def reverse(string: str):  # print(reverse("hello"))
    result = ""
    
    for index in range(len(string) - 1, -1, -1):
        result += string[index]
        
    return result


def reverse_recursive(string: str): # print(reverse_recursive("apple"))
    if not string:
        return ""
    
    return string[-1] + reverse_recursive(string[:len(string)-1])


def count_char_recursive(string: str):  # print(count_char_recursive("apple"))
    if not string:
        return 0
    
    return 1 + count_char_recursive(string[:len(string)-1])


def remove_char_recursive(string:str, target:str):  # print(remove_char_recursive("apple", "p"))
    if not string:
        return ""
    
    if string[0] == target:
        return remove_char_recursive(string[1:], target)
    
    return string[0] + remove_char_recursive(string[1:], target)


def is_palindrome_recursion(string):  # print(is_palindrome_recursion(""))
    if len(string) <= 1:
        return True
    
    if string[0] != string[-1]:
        return False
    
    return is_palindrome_recursion(string[1:-1])


def is_palindrome_recursion_2(string: str, left: int = 0, right: int | None = None) -> bool: # print(is_palindrome_recursion_2("racecar"))
    # Initialize the right pointer on the first call
    if right is None:
        right = len(string) - 1
        
    # Base Case: Pointers have met or crossed -> valid palindrome
    if left >= right:
        return True
    
    # Base Case: Characters at pointers do not match -> not a palindrome
    if string[left] != string[right]:
        return False
    
    # Recurse with left pointer moved right and right pointer moved left
    return is_palindrome_recursion(string, left + 1, right - 1) # type: ignore


def find_maximum_recursive(arr: list): #print(find_maximum_recursive([9, 22, 34]))
    # Base Case 1: Empty list
    if not arr:
        return -1
    
    # Base Case 2: Single element left
    if len(arr) == 1:
        return arr[0]
    
    # Recurse on the rest of the list
    max_of_rest = find_maximum_recursive(arr[1:])
    
    # Compare current element with maximum of the rest
    return arr[0] if arr[0] > max_of_rest else max_of_rest  # noqa: FURB136


def find_max(nums: list[int]):
    num = float("-inf")
    
    for n in nums:
        if n > num:  # noqa: PLR1730
            num = n
    
    return num


def find_min_recursive(arr: list[int]): # print(find_min_recursive([x for x in range(10)]))
    if not arr:
        return -1
    
    if len(arr) == 1:
        return arr[0]
    
    minimum = find_min_recursive(arr[1:])
    
    return arr[0] if arr[0] < minimum else minimum  # noqa: FURB136


def sum_of_list_recursive(arr: list[int]): # print(sum_of_list_recursive([1, 2, 3, 4, 5]))
    if not arr:
        return -1
    
    if len(arr) == 1:
        return arr[0]
    
    return arr[0] + sum_of_list_recursive(arr[1:])


def count_positive_nums(arr: list[int]): # print(count_positive_nums([-2, 3, 0, 4, 9, -6]))
    if not arr:
        return 0
    
    if arr[0] > 0:
        return 1 + count_positive_nums(arr[1:])
    
    return count_positive_nums(arr[1:])


def linear_search_recursive(arr: list[int], target: int, index=0): # print(linear_search_recursive([4, 7, 2, 9], 9))
    if len(arr) == index:
        return False
    
    if arr[index] == target:
        return True
    
    return linear_search_recursive(arr, target, index+1)


def find_index_recursive(arr: list[int], target: int, index = 0): # print(find_index_recursive([10, 20, 30, 40], 30))
    if len(arr) == index:
        return -1
    
    if arr[index] == target:
        return index
    
    return find_index_recursive(arr, target, index+1)
