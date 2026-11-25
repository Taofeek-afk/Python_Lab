# Countdown

def countdown(n: int) -> None: # countdown(5)
    
    while n >= 1:
        print(n)
        n -= 1

def recursive_countdown(n: int) -> None: # recursive_countdown(5)
    if n <= 0:
        return
    
    print(n)
    
    return recursive_countdown(n - 1)


# count up

def recursive_countup(n: int) -> None: # recursive_countup(5)
    if n <= 0:
        return
    
    recursive_countup(n - 1)
    print(n)


# Sum to N

def sum_to_n(n: int): # print(sum_to_n(5))
    sum = 0
    
    while n >= 0:  # for n in range(1, n+1):
        sum += n   #    sum += n
        n -= 1
        
    return sum

def recursive_sum_to_n(n: int): # print(recursive_sum_to_n(5))
    if n <= 0:
        return 0
    
    return n + recursive_sum_to_n(n - 1)


# Factorial

def factorial(n: int):  # print(factorial(5))
    if n <= 0:
        return -1
    
    for num in range(1, n):
        n *= num
    
    return n

def recursive_facorial(n: int):  # print(recursive_facorial(5))
    if n <= 0:
        return 1
    
    return n * recursive_facorial(n - 1)


# Power

def self_power(n: int, exponent: int): # print(self_power(2, 5))
    if exponent <= 0:
        return 1
    
    num = n
    
    for _ in range(exponent-1):
        num *= n
        
    return num

def recursive_power(n: int, exponent: int):  # print(recursive_power(2, 5))
    if exponent <= 0:
        return 1
    
    return n * recursive_power(n, exponent - 1)

    # No edge cases handled


# product range
def product_range(start: int, stop: int): # print(product_range(3, 6))
    for num in range(start+1, stop+1):
        start *= num
    
    return start

def recursive_product_range(start: int, stop: int):  # print(recursive_product_range(3, 6))
    if start == stop+1:
        return 1
    
    return start * recursive_product_range(start+1, stop)


# sum of even num
def recursive_sum_even(n:int):  # print(recursive_sum_even(9))
    if n <= 0:
        return 0
    
    if n % 2 != 0:
        n -= 1
    
    return n + recursive_sum_even(n-2)

def recursive_sum_even_2(n:int):  # print(recursive_sum_even_2(10))
    if n <= 0:
        return 0
    
    if n % 2 == 0:
        return n + recursive_sum_even_2(n - 1)
    else:
        return recursive_sum_even_2(n-1)


# Count digits
def count_digits(n):
    if n < 10:
        return 1
    
    count = 0
    
    while n != 0:
        n //= 10
        count += 1
    
    return count

def recursive_count_digits(n):  # print(recursive_count_digits(-23333))
    n = abs(n)
    
    if n < 10:
        return 1
    
    
    return 1 + recursive_count_digits(n // 10)


# sum of digits
def recursive_sum_digits(n):  # print(recursive_sum_digits(2244))
    n = abs(n)
    
    if n <= 0:
        return 0
    
    return n % 10 + recursive_sum_digits(n // 10)

    # n = abs(n)
    # sum = 0
    # while n > 0:
    #     sum += n % 10
    #     n //= 10

    
    # return sum


# Reverse an integer; 1234 = 4321

def reverse_num(n): # print(reverse_num(1235))

    sign = -1 if n < 0 else 1
    n = abs(n)
    
    rev_num = 0
    
    while n > 0:
        last_digit = n % 10
        rev_num = (rev_num * 10) + last_digit
        # print(rev_num)
        n //= 10
        
    return rev_num * sign

def reverse_recursive(num: int, result: int = 0):  # print(reverse_recursive(123))
    if num <= 0:
        return result
    
    last_digit = num % 10
    result = (result * 10) + last_digit
    
    return reverse_recursive(num // 10, result)


# def recursive_reverse_num(n: int) -> int:
#     # Preserve negative sign if needed
#     sign = -1 if n < 0 else 1
    
#     def helper(num: int, rev: int) -> int:
#         if num == 0:
#             return rev
        
#         last_digit = num % 10
#         # Shift existing reversed value left by 10, then add last_digit
#         return helper(num // 10, (rev * 10) + last_digit)

#     return sign * helper(abs(n), 0)


# print(recursive_reverse_num(1234))  # Output: 4321
