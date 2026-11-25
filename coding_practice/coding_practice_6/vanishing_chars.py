def vanishing_characters(string: str):
    
    n = 1
    
    while n < len(string):
        if string[n] == string[n-1]:
            if n-1 == 0:
                string = string[n+2:]
            elif n == len(string)-1:
                string = string[0:len(string)-2]
        
        n += 1
    
    return string


print(vanishing_characters("aaaaaa"))
