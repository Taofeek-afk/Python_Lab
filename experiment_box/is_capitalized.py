def is_capitalized(string: str):
    if len(string) == 0:
        return False
    
    for char in range(len(string)):
        if string[char-1] == " ":
            if ord(string[char]) >= 97 and ord(string[char]) <= 122:
                return False
    return True         
        
print(is_capitalized("Hello! How are you?"))
print(is_capitalized("Hello How Are You?"))
print(is_capitalized("Whats 4this 100k"))
print(is_capitalized("Whatsthis4"))
print(is_capitalized("!!!Whatsthis4"))
print(is_capitalized(""))


# Compare with alphabets, check the first index explicitly then increase the range start to 1