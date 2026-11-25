def sum_of_factorial(nums):
    y = 1

    for n in nums[:len(nums):4]:
        y *= int(n)
        
    return y


def print_factorials(n=8):
    """This functions print factorials for nums between 1 to 9"""

    nums = "1"
    y = 1
    
    if n <= 1:
        return n
    
    print(1)
    for i in range(2, n+1):
        nums += f" * {i}"
        y = sum_of_factorial(nums)
        
        if i != n:
            print(f"{nums} = {y}")
    
    return f"{nums} = {y}"

# print(print_factorials(9))
