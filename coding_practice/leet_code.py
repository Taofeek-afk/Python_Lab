# parentheses = [("(", ")"), ("[", "]"), ("{", "}")]

# def is_valid_parentheses(string: str):
#     left = 0
#     right = len(string) - 1
#     bracket = ""
#     switch = "off"
    
#     while left <= right:
#         for value in parentheses:
#             if string[left] == value[0]:
#                 bracket = value[1]
#                 switch = "on"
#                 break
#             elif string[left] == value[1]:
#                 return False
        
#         left += 1
#         # print(switch)
#         for value in parentheses:
#             if string[right] == value[0]:
#                 return False
#             elif string[right] == value[1]:
#                 if string[right] != bracket:
#                     return False
#                 else:
#                     switch = "off"
#                     break
        
#         right -= 1

#     return switch != "on"

# tests = [
#     "()()",
#     "()[]",
#     # "{}{}",
#     # "([{}])abc",
# ]

# print(is_valid_parentheses("()()"))


def is_valid_parentheses(string: str) -> bool:
    stack = []
    pairs = {
        ")":"(",
        "}":"{",
        "]":"["
    }
    
    for char in string:
        if char in "({[":
            stack.append(char)
        elif char in "})]" and (not stack or stack.pop() != pairs[char]):
            return False
        
    return not stack


# print(is_valid_parentheses("()[bbbbbb]){}"))


def merge_two_lists(list1: list, list2: list):
    i = 0
    j = 0
    
    merged_list = []
    
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    
    if i < len(list1):
        merged_list.extend(list1[i:])
    
    if j < len(list2):
        merged_list.extend(list2[j:])
    
    return merged_list



# print(merge_two_lists([1, 3, 7, 9, 43, 78], [2, 7, 9, 13]))


def remove_duplicates(arr):  # Not main question
    if not arr or len(arr) == 1:
        return arr
    
    container = []
    highest = arr[len(arr)-1]
    arr.append(float("inf"))
    
    n = 0
    
    while n < len(arr):
        if arr[n] != arr[n+1]:
            container.append(arr[n])
            if arr[n] == highest:
                break

        n += 1

    return container


nums = [1, 1, 3, 3, 7, 7, 7, 7, 9, 11, 12, 122, 122, 122, 123, 123, 123, 129, 176]
# print(remove_duplicates(nums))


def remove_duplicates_in_place(arr: list[int]):
    n = 1
    index = 1
    
    while n < len(arr):
        if arr[n] != arr[n-1]:
            arr[index] = arr[n]
            index += 1

        n += 1
    
    return index


k = remove_duplicates_in_place(nums)
# print(nums[:k])


def remove_duplicates_unsorted(arr: list[int]): # Don't use a set: not main question
    index = 1
    for n in range(1, len(arr)):
        for i in range(n):
            if arr[i] == arr[n]:
                break
        else:
            arr[index] = arr[n]
            index += 1
            
    if len(arr[:index]) != len(set(arr)):
        raise RuntimeError("Incorrect implementaion")

    return arr[:index]


# print(remove_duplicates_unsorted([3, 99, 3, 7, 2, 12, 9, 3, 8, 9, 4, 2]))

def find(sentence: str, word: str):  # recursion
    if not sentence:
        return False
    
    if sentence[:len(word)] == word:
        return True

    return find(sentence[1:], word)


# print(find(haystack, needle))


nums = [0,1,2,2,3,0,4,2]
val = 2

# 0, 1, 3, 0, 4

def remove_element(value: list[int], num: int): # 3
    n = 0
    index = 0
    
    while n < len(value):
        if value[n] != num:
            value[index] = value[n]
            index += 1
        n += 1
    
    # print(index)
    return (value[:index], index) # return index
 

# print(remove_element(nums, val))


def search_insert(num: list[int], target):
    for n in range(len(num)):
        if num[n] == target:
            return n

    return len(num)

# print(search_insert(nums, 12))


def last_word(sentence: str): 
    last_word = ""
    word = ""
    
    for n in range(len(sentence)):
        if sentence[n] != " ":
            last_word += sentence[n]
        elif sentence[n] == " " and last_word:
            word = last_word
            last_word = ""
    
    return last_word or word or None


def last_word_2(sentence: str):
    last_word = ""
    
    for n in range(len(sentence)-1, -1, -1):
        if sentence[n] == " " and last_word:
            return "".join(reversed(last_word))
        elif sentence[n] != " ":
            last_word += sentence[n]
    
        
# print(last_word_2("     abb  kj{}    "))

# def plus_one(arr: list[int]):
#     if not arr:
#         return False

#     last_index = len(arr)-1
    
#     if arr[last_index] < 9:
#         arr[last_index] += 1
#     elif len(str(arr[last_index] + 1)) > len(str(arr[last_index])):
#         extension = [int(x) for x in str(arr[last_index] + 1)]
#         arr.pop()
#         arr.extend(extension)
#     else:
#         arr[last_index] += 1

#     return arr


def plus_one_2(arr: list[int]):
    if not arr:
        return arr
    
    last_index = len(arr) - 1
    
    # Simple case: last digit is not 9
    if arr[last_index] != 9:
        arr[last_index] += 1
        return arr
    else:
        # 1. Convert entire array to integer
        num = 0
        for digit in arr: # [1, 2, 3, 9]
            num = num * 10 + digit
            
        # 2. Add 1
        num += 1
        
        # 3. Reconstruct array from digits
        result = []
        while num > 0:
            result.append(num % 10)
            num //= 10
            
        # Digits were collected right-to-left, so reverse them back
        result.reverse()
        return result    


def plus_one(arr: list[int]) -> list[int]:
    # Iterate backwards through the array
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] < 9:
            arr[i] += 1
            return arr
        # If digit is 9, it becomes 0 and we carry the 1 to the left
        arr[i] = 0

    # If all digits were 9 (e.g., [9, 9] -> [0, 0]), prepend a 1
    print(arr)
    return [1] + arr


digits = [8, 7, 9]
# print(plus_one_2(digits))

def get_window(num: int):
    n = count = 0

    while 2 ** n <= num:
        n += 1
        count += 1
    
    return count
# print(get_window(7))

def convert_binary(a: str):
    'This function converts binaries to base 10 in int format'
    counter = num = 0
    exponent = 2
    for n in range(len(a)-1, -1, -1):
        if a[n] == "1":
            num += (exponent ** counter)
        counter += 1  # noqa: SIM113
         
    return num


def add_binary(a, b):
    return convert_binary(a) + convert_binary(b)


def convert_to_binary(num=15):
    remainder = ""
    while num != 0:
        remainder += str(num % 2)
        num //= 2


    return "".join(reversed(remainder))


# print(convert_to_binary(add_binary("1010", "1011")))
# print(count)

# Input: a = "11", b = "1" 
# Output: "100"

# Input: a = "1010", b = "1011"
# Output: "10101"
# 1 + 2 + 1 = 4


n = 5

for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
