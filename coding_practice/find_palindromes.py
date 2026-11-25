# just do it

# sliding window
def is_palindrome_1(string: str):
    if not string:
        return ""

    return sorted(string[len(string)//2:]) == sorted(string[:len(string)//2] ) or sorted(string[(len(string)//2)+1:]) == sorted(string[:len(string)//2])


# print(is_palindrome_1("sass"))


# Two pointers
def is_palindrome_2(string: str):
    if not string: return None
    
    left = 0
    right = len(string)-1
    
    while left < right:
        if string[left] != string[right]:
            return f"{string} is not a palindrome"
        
        left += 1
        right -= 1
    
    return f"{string} is a palindrome"


# print(is_palindrome_2("racecar"))


# manual convention
def is_palindrome_3(string: str):
    if not string:
        return None
    
    reversed_string = ""
    
    for char in string:
        reversed_string = char + reversed_string
        print(reversed_string)
    
    
    return string == reversed_string    


# print(is_palindrome_3("abbaa"))


# double two pointers -- for extremely long or long strings
def is_palindrome_4(string: str):
    if not string:
        return None
    
    left = 0 # first index
    right = len(string) - 1 # last index
    
    if len(string) % 2: # if length of string is odd.
        foremost_left = len(string) // 2 - 1 # The first index to the left after the length of the string is floor divided into 2
        foremost_right = len(string) // 2 + 1 # The first index to the right after the length of the string is floor divided into 2
    else: # if length of string is even
        foremost_left = len(string) // 2
        foremost_right = len(string) // 2
        
    
    while left < right:
        if string[left] != string[right] or string[foremost_left] != string[foremost_right]: 
            return f"{string} is not a palindrome"
        
        left += 1
        right -= 1
        
        foremost_left += 1
        foremost_right -= 1
    
    return f"{string} is a palindrome"


# print(is_palindrome_4("bab")) 


# recursive is_palindrome
def is_palindrome_5(string: str):
    if not string: return True
    
    if string[0] != string[len(string)-1]:
        return False
    
    return is_palindrome_5(string[1:len(string)-1])


# print(is_palindrome_5("rar"))
