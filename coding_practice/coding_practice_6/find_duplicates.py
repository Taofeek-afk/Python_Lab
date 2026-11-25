input = [1, 2, 3, 3, 2, 4, 5, 1] # 1, 2

def find_duplicates(nums: list[int] = input):

    seen = {}
    
    for n in nums:
        seen[n] = seen.get(n, 0) + 1
            
    duplicates = [n for n in seen if seen[n] > 1]

    return duplicates

print(find_duplicates())
