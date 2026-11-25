def two_sum(arr, target):
    for n in range(len(arr)):
        # if arr[n] == target:
        #     return n
        for j in range(n):
            if arr[n] + arr[j] == target:
                return (arr[j], arr[n])
    
    return -1
            

# print(two_sum([2, 7, 11, 15], 9))
# print(two_sum([3, 8, 4, 6], 10))


# to_learn
def two_sum_2(arr, target):
    seen = set() # 2, 7, 
    for num in arr:
        complement = target - num
        print(complement)
        if complement in seen:
            return (complement, num)
        seen.add(num)
    
    return -1
# why it works: if target - num in a for loop == a num, that's it
# print(two_sum_2([2, 7, 11, 15], 18))


def two_sum_3(arr, target):
    seen = {}  # Maps value -> index
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i
    
    return -1


# print(two_sum_3)
