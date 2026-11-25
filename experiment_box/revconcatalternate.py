def reverse(obj):  # list, tuple, and string
    if not isinstance(obj, (str, list, tuple)):
        return obj

    reversed_obj = type(obj)()

    if isinstance(obj, str):
        for i in obj:
            reversed_obj = i + reversed_obj # type: ignore
    else:
        for i in obj:
            reversed_obj = type(obj)([i]) + reversed_obj # type: ignore
    
    return reversed_obj




def revconcatalternate(item_1: str, item_2: str):
    item_1, item_2 = reverse(item_1), reverse(item_2)
    total_items = ""
    
        
    for i in item_1:
        total_items += i
        
    return 0
    
    
    

# 1, 2, 3, 4, 5; 6, 7, 8, 9, 10 = 5, 10, 4, 9, 3, 8, 2, 7, 1, 6
# 5, 4, 3, 2, 1; 10, 9, 8, 7, 6. first index from each value. 
        
# def reverse(obj):
#     items = list(obj)
    
#     # 2. Two-pointer swap loop
#     low = 0
#     high = len(items) - 1
#     while low < high:
#         items[low], items[high] = items[high], items[low]
#         low += 1
#         high -= 1
        
#     # 3. Handle types dynamically
#     if isinstance(obj, str):
#         return "".join(items)
        
#     try:
#         # Try using the original class constructor (works for list, tuple)
#         return type(obj)(items)
#     except TypeError:
#         # Fallback for generators, ranges, or objects that don't accept lists
#         return items


# print(reverse("apple"))
