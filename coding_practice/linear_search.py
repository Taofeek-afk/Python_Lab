def linear_search(arr: list[int], target: int) -> int|None:
    for i, n in enumerate(arr):
        if n == target:
            return i
    return None

array = [14, 7, 22, 22, 7, 31]
print(linear_search(array, 22))

