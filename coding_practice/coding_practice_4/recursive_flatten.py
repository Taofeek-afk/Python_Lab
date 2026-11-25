def flatten(arr: list[int | list], container: list):
    if not arr:
        return container
    
    if type(arr[0]) == list:  # if isinstance(arr[0], list): ... 
        return flatten(arr[0], container)
    
    container.append(arr[0])
    
    return flatten(arr[1:], container)
    
# print(flatten([1, 2, 3, 4, [2, 7, 8]], []))  # check

# print(type(6) == str)
def group_by(items, func = lambda w: w[0]):
    items = flatten(items, [])
    container = {}
    
    for item in items:
        if item[0] not in container:
            container[item[0]] = [item]
        else:
            container[item[0]].append(item)
            
    return dict(sorted(container.items(), key=func))


# print(group_by(["pple", "leap", "grip", "apply", "appear", "jaguar"]))
