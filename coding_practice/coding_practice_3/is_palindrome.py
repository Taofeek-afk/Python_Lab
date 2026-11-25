def is_palindrome(string: str):
    string = string.lower()
    
    left_string = ""
    right_string = ""
    punctuations = "!?, ."
    
    for n in range(len(string)//2):
        if string[n] not in punctuations:
            left_string += string[n]
    
    for n in range(len(string)//2-1,len(string)):
        if string[n] not in punctuations:
            right_string += string[n]
        
    if left_string == right_string:
        return "Palindrome"
    
    return "Not a Palindrome"


# print(is_palindrome("Was saw?"))
# print(len("Was it a car o"))
