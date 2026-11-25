def two_sum(nums: list[int], target: int):
    seen = {}
    
    for i, n in enumerate(nums):
        if target - n in seen:
            return i, seen[target-n]
        seen[n] = i
    
    return []


print(two_sum([2, 7, 11, 15], 118))
