

items = ["apple", "propaganda", "egg", "chariot", "dumpsies", "entourage", "carriage", "plant"]

def get_max_length(arr: list):
    max = ""
    
    for item in range(len(arr)):
        if len(arr[item]) > len(max):
            max = arr[item]

    return max


# print(get_max(items))

def get_second_largest_item(arr: list):
    largest = ""
    sec_max = ""
    
    for n in range(len(arr)):
        if len(arr[n]) > len(largest):
            sec_max = largest
            largest =  arr[n]
        elif len(arr[n]) > len(sec_max) and len(arr[n]) != len(largest):
            sec_max = arr[n]

    return largest, sec_max 


# print(get_second_largest_item(items))


def rotate_left(arr, step):
    n = len(arr)
    result = [0] * n
    # print(result)

    for i in range(n):
        new_index = (i - step) % n
        result[new_index] = arr[i]

    return result


items = [1, 2, 3, 4, 5]
# print(rotate_left(items, 9))


def remove_duplicates(arr: list):
    result = []
    
    for i in range(len(arr)):
        exists = False
        for n in range(len(result)):
            if arr[i] == result[n]:
                exists = True
                break
        
        if not exists:
            result.append(arr[i])
        
    return result

# print(remove_duplicates([1, 2, 1, 4, 3, 5, 7, 2]))

            
# * Rotate a list. left rotation, by three steps.

def move_all_zeros_to_the_end(arr: list):
    result = []
    for i in range(len(arr)):
        if arr[i] != 0:
            result.append(arr[i])
    
    for i in range(len(arr)):
        if arr[i] == 0:
            result.append(0)
    
    
    return result

# print(move_all_zeros_to_the_end([0, 1, 3, 0, 8, 0, 3, 9]))


# def move_all_zeros_to_the_end(arr):
#     result = []
#     zeros = 0

#     for item in arr:
#         if item == 0:
#             zeros += 1
#         else:
#             result.append(item)

#     result.extend([0] * zeros)
#     return result



def get_zero_to_the_end(arr: list):
    for i in range(len(arr)):
        while i < len(arr) - 1 and (arr[i] == 0 and arr[i+1] >= 0):
            temp = arr[i]
            arr[i], arr[i+1] = arr[i+1], temp
            i += 1
            
    return arr


# print(get_zero_to_the_end([0, 1, 3, 0, 8, 0, 3, 9]))


def get_zero_to_the_end_2(arr: list):  # If position does not matter
    i = len(arr) - 1
    count = 1
    
    while i >= 0:
        if arr[i] == 0 and i != len(arr) - count:
          temp = arr[len(arr) - count]
          arr[len(arr) - count], arr[i] = arr[i], temp
          count += 1
        i -= 1
    
    return arr


# print(get_zero_to_the_end_2([0, 1, 3, 0, 8, 0, 3, 9]))
# def get_zero_to_the_end_2(arr):
#     end = len(arr) - 1

#     i = end
#     while i >= 0:
#         if arr[i] == 0 and i != end:
#             arr[i], arr[end] = arr[end], arr[i]
#             end -= 1
#         i -= 1

#     return arr

def move_zeros(arr):
    write = 0
    
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[write] = arr[i]
            write += 1
    
    while write < len(arr):
        arr[write] = 0
        write += 1
        
    return arr

# print(move_zeros([0, 1, 3, 0, 8, 0, 3, 9]))


def find_mising_nums(arr: list):
    missing_nums = []
    # sort the list. or Get the min and max values first
    for i in range(len(arr)-1):
        
        min_index = i
        
        for n in range(i+1, len(arr)):
            if arr[n] < arr[min_index]:
                arr[n], arr[min_index] = arr[min_index], arr[n]
    
    for i in range(len(arr)-1):
        missing_nums.extend(range(arr[i]+1, arr[i+1]))
        print(arr[i]+1, arr[i+1])
    
    return missing_nums
            


# print(find_mising_nums([0, 1, 3, 0, 8, 0, 3, 9]))


def find_missing_nums_2(arr):
    missing_nums = []

    # Selection Sort
    for i in range(len(arr) - 1):
        min_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
                print(min_index)

        if min_index != i:   
            print(i)# only swap if needed
            arr[i], arr[min_index] = arr[min_index], arr[i]

    # Find missing numbers
    for i in range(len(arr) - 1):
        for num in range(arr[i] + 1, arr[i + 1]):
            missing_nums.append(num)  # noqa: PERF402

    return missing_nums

print(find_missing_nums_2([[0, 1, 3, 0, 8, 0, 3, 9]]))


def merge_sorted_arrays(arr_1: list, arr_2: list):
    i = 0
    j = 0
    container = []

    while i < len(arr_1) and j < len(arr_2):
        if arr_1[i] <= arr_2[j]:
            container.append(arr_1[i])
            i += 1
        else:
            container.append(arr_2[j])
            j += 1

    # Add whatever is left
    container.extend(arr_1[i:])
    container.extend(arr_2[j:])

    return container


print(merge_sorted_arrays(
    [1, 2, 3, 4, 5, 6],
    [5, 9, 11, 23]
))


# print(merge_sorted_arrays([1, 2, 3, 4, 5, 6], [5, 9, 11, 23]))


def merge_sorted_arrays_2(arr_1: list, arr_2: list):
    
    i = 0
    j = 0
    
    container: list = []
    
    while i < len(arr_1) and j < len(arr_2):
        
        if arr_1[i] <= arr_2[j]:
            # print(arr_1[i])
            container.append(arr_1[i])
            i += 1
            # j += 1
        elif arr_2[j] <= arr_1[i]:
            # print(arr_2[j])
            container.append(arr_2[j])
            j += 1
            # i += 1
    
    if i < len(arr_1):
        container.extend(arr_1[i:])
        
    if j < len(arr_2):
        container.extend(arr_2[j:])
    
    return container


print(merge_sorted_arrays_2([1,], [5, 9, 11, 23]))


def track_highest_and_second_highest(arr: list):
    if len(arr) == 0:
        return -1
    
    max = arr[0]
    sec_max = float("-inf")  # Correction
    
    for i in range(1, len(arr)):
        if arr[i] > max:
            sec_max = max
            max = arr[i]
        elif arr[i] < max and arr[i] > sec_max:
            sec_max = arr[i]
    
    return max, sec_max



print(track_highest_and_second_highest([5, 4, 3, 9, 13, 24, 17]))


def keep_two_shortest_paths(arr: list):
    if len(arr) == 0:
        return -1
    
    
    min = arr[0]
    sec_min = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] < min:
            sec_min = min
            min = arr[i]
        elif arr[i] > min and arr[i] < sec_min:
            sec_min = arr[i]
    
    if min == sec_min:
        sec_min = -1  # No sec minimum was found

    return min, sec_min


print(keep_two_shortest_paths([3, 3, 3, 3]))
            

def longest_sequence_of_vowels(string: str):
    vowels = "aeiou"
    count = 0
    longest = 0
    
    for i in range(len(string)):
        for j in range(len(vowels)):
            if string[i] == vowels[j]:
                count += 1
                break
        else:
            longest = count if count > longest else longest  # noqa: FURB136
            count = 0
        
    return longest


print(longest_sequence_of_vowels("aeioubhh."))


sec_max = float("-inf")
print(type(sec_max))


