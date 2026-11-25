def is_prime(n):
    if n <= 1:
        return False

    if n == 2:
        return True

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def previous_prime(n: int) -> bool | int:
    if n <= 1:
        return 0

    if n == 2:
        return True

    prev_num = n - 1

    while prev_num < n and prev_num > 1:
        if is_prime(prev_num):
            return prev_num
        prev_num -= 1

    return 


print(previous_prime(1))
