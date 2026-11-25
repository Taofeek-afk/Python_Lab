def binary_search_recursive(arr, target, left, right): # print(binary_search_recursive([1, 2, 3, 4, 5, 6, 7, 8, 9], 5, left=0, right=len([1, 2, 3, 4, 5, 6, 7, 8, 9])-1))
    if left > right:
        return -1
    
    mid = (left+right) // 2
        
    if arr[mid] == target:
        return mid
    elif target > arr[mid]: 
        left = mid + 1
    else:
        right = mid - 1
        
    return binary_search_recursive(arr, target, left, right)


def binary_search(arr, target):  # print(binary_search([1, 2, 3], 2))

    if not arr:
        return -1
    
    right, left = len(arr)-1, 0
    
    while left <= right:
        mid = (right + left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return - 1


def string_binary_search_recursive(arr, target, left, right): # As long as the list is sorted, binary search can compare strings, like b > a, since b is after a, making it suitable fo searching sorted elements.
    ...
    

def first_occurence(arr, target): # print(first_occurence([1, 2, 2, 2, 4, 5], 2)) ... Didn't meet the problem requirement
    index = binary_search_recursive(arr, target, left=0, right=len(arr)-1)
        
    while index > 0 and arr[index-1] == arr[index]:
        index -= 1
    
    return index


def first_occurence_recursive(arr, target, left, right): # print(first_occurence_recursive([1, 2, 2, 2, 3, 4, 4, 4, 4, 4, 5], 4, 0, len([1, 2, 2, 2, 4, 5]) - 1))
    if left > right:
        return -1 
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        earlier = first_occurence_recursive(arr, target, left, mid-1)
        return mid if earlier == -1 else earlier
    
    elif target < arr[mid]:
        return first_occurence_recursive(arr, target, left, mid-1)

    else:
        return first_occurence_recursive(arr, target, mid + 1, right)


def last_occurence_recursive(arr, target, left, right): # arr = [1, 2, 2, 2, 4, 5] print(last_occurence_recursive(arr, 5, 0, len(arr)-1))

    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        latest = last_occurence_recursive(arr, target, mid+1, right)
        return latest if latest != -1 else mid
    
    elif arr[mid] < target:
        return last_occurence_recursive(arr, target, mid+1, right)

    else:
        return last_occurence_recursive(arr, target, left, mid-1)


def count_occurence_recursive(arr, target, left, right):  # ???
    
    def find_first(left, right):
        if left > right:
            return -1
    
        mid = (left + right) // 2
    
        if arr[mid] == target:
            earlier = find_first(left, mid - 1)
            return mid if earlier == -1 else earlier

        elif arr[mid] > target:
            return find_first(left, mid - 1)

        else:
            return find_first(mid + 1, right)
        
    def find_last(left, right):
        if left > right:
            return -1

        mid = (left + right) // 2

        if arr[mid] == target:
            later = find_last(mid + 1, right)

            if later == -1:
                return mid
            return later

        elif arr[mid] > target:
            return find_last(left, mid - 1)

        else:
            return find_last(mid + 1, right)

    first = find_first(left, right)

    if first == -1:
        return 0

    last = find_last(left, right)

    return last - first + 1


arr = [1, 2, 2, 2, 4, 5]

print(count_occurence_recursive(arr, 2, 0, len(arr) - 1))
print(count_occurence_recursive([1, 2, 3, 4, 5], 2, 0, len([1, 2, 3, 4, 5]) - 1))
