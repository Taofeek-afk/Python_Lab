def we_are_unique(string_1, string_2):
    if string_1 and string_2 == 0:
        return -1
    
    container = ""
    
    for char in string_1:
        for c in string_2:
            if char in container:  # Helper function in C
                continue
            if char != c:
                container += char
    
    for char in string_2:
        for c in string_1:
            if char in container:
                continue
            if char != c:
                container += char

    return len(container)

#  Write a program that takes two strings 
# and returns the number of characters that are not included in both without repeating characters.


print(we_are_unique("ab111cc", "daaacef"))
