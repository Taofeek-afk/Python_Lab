def second_largest(arr):
    largest = arr[0]
    second_largest = float("-inf")
    
    for n in arr[1:]:
        if n > largest:
            largest = n
        elif largest > n > second_largest:
            second_largest = n
            
    return second_largest


print(second_largest([10, 20, 8, 20, 15]))
