def two_sum(arr, target):
    
    nums = {}
    
    for i, n in enumerate(arr):
        print(nums)
        if target - n in nums:
            return nums[target-n], i
        else:
            nums[n] = i


print(two_sum([2, 7, 15, 45], 17))

# if n not in arr, append to it. if target - next value in dict return indexes. 
