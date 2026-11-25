# Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not return the index where it would be if it were inserted in order

num = [1, 3, 5, 6,]  
# where target is 5, index would be 2. 
# if target is 2, index would be 1. 
# if target not in list target would be length of array


def get_position(num: list, target: int) :
 
    for i in range(len(num)):
        if num[i] == target or num[i] > target:
            return i

    return len(num)
        

print(get_position([1, 3, 5, 6], 7))
