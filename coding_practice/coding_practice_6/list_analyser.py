numbers = [12, 5, 27, 8, 14, 27, 3]

def list_analyser(nums: list[int] = numbers) -> str:
    largest = nums[0], 0
    smallest = float("inf"), None
    total = 0

    for i, n in enumerate(nums):        
        if n > largest[0]:
            largest = n, i
        
        if n < smallest[0]:
            smallest = n, i
        
        total += n
    
    average = round(total/len(nums), 2)
    
    above_average = [x for x in nums if x > average]
    
    return f"Smallest: {smallest[0]} (at index {smallest[1]})\nLargest: {largest[0]} (at index {largest[1]})\nTotal: {total}\nAverage: {average}\nNumbers above average: {len(above_average)} ({above_average})"

print(list_analyser())   
