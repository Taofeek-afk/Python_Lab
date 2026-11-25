# # * Factorial.
# # * Fibonacci.
# # * Sum of digits.
# # * Reverse a string recursively.
# # * Binary search.


# def countdown(n: int):
#     if n <= 0:
#         return 0
    
#     print(n)
#     num = countdown(n-1)
#     return num



# # print(countdown(5))


# def count_up(n: int):
#     if n <= 0:
#         return 0


#     num = count_up(n-1)
#     print(n)
    
#     return num
    

# # print(count_up(5))


# def sum_to_n(n: int):
#     if n <= 0:
#         return 0
    
#     return n + sum_to_n(n-1)


# # print(sum_to_n(5))


# def factorial(n: int):
#     # 5 × 4 × 3 × 2 × 1 = 120
#     if n < 1:
#         return 1
    

#     return n * factorial(n-1)


# # print(factorial(5))


# # def list_length(arr): 
#     # Base case: an empty list has length 0
#     if not arr:
#         return 0

#     # 1 for the current item + length of the rest of the list
#     return 1 + list_length(arr[1:])


# # print(list_length([1, 2, 3, 4, 5]))  # Output: 5


# def list_length(arr, n=0):
#     if not arr:
#         return n

#     return list_length(arr[1:], n + 1)


# print(list_length([1, 2, 3, 4, 5]))  # Output: 5


# def find_max(arr):
#     # Base case 1: empty list
#     if not arr:
#         return None

#     # Base case 2: single-element list
#     if len(arr) == 1:
#         return arr[0]

#     # Recursive step: slice off the first element arr[1:]
#     max_of_rest = find_max(arr[1:])

#     # Return the larger of the first element vs the max of the rest
#     return arr[0] if arr[0] > max_of_rest else max_of_rest


# print(find_max([3, 1, 9, 4, 7]))  # Output: 9
