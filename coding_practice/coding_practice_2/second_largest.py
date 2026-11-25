def second_largest(arr):
    largest = max(arr)
    print(largest)
    num = float("-inf")
    
    for n in arr:
        if n > num and n != largest:
            num = n
    
    return num


print(second_largest([10, 5, 8, 20, 15]))
print(second_largest([4, 9, 2, 9, 7]))
print(second_largest([3, 3, 3, 3,]))
