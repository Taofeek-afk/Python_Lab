nums = [12, 5, 27, 8, 14]

def list_analyser(arr = nums):
    smallest = float("inf")
    largest = arr[0]
    total = 0
    
    for n in nums:
        if n < smallest:  # noqa: PLR1730
            smallest = n
        if n > largest:  # noqa: PLR1730
            largest = n
            
        total += n
    
    average = total / len(arr)
    
    return f"Smallest: {smallest}, Largest: {largest}, Total: {total}, Average: {average}"


print(list_analyser())


smallest = float("inf")
largest = float("-inf")
total = 0

# smallest, largest, total = [n if n < smallest else 9 f]
