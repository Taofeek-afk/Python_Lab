def is_palindrome(word: str):
    
    word = word.lower()
    print(word)
    
    left = 0
    right = len(word) - 1
    
    punctuations = [" ,?!."]
    
    while left < right:
        
        while left < right:
            if word[left] in punctuations:
                left += 1
            else:
                break
            
        while left < right:
            if word[right] in punctuations:
                right -= 1
            else:
                break
            
        if word[left] != word[right]:
            return "Not a palindrome"
    
    left += 1
    right -= 1
    
    return "Palindrome"


# print(is_palindrome("Was it a car or a cat I saw?"))
# print(is_palindrome("Hello, World!"))
# print(is_palindrome("racecar"))
# print(is_palindrome("Was it a car or a cat I saw?"))


def is_palindrome_2(word):
    
    word = "".join([x.lower() for x in word if x.isalnum()])
    # print(word)
    
    left = len(word)
    right = 0
    
    while left < right:
        if word[left] != word[right]:
            return "Not a palindrome"
        
        left += 1
        right -= 1
        
    return "Palindrome"    

# print(is_palindrome_2("Was it a car or a cat I saw?"))


def is_palindrome_3(word):
    if not word:
        return "Palindrome"
    
    if not word[0].isalnum():
        return is_palindrome_3(word[1:])
    
    if not word[len(word)-1].isalnum():
        return is_palindrome_3(word[:len(word)-1])
    
    if word[0].lower() != word[len(word)-1].lower():
        return "Not a palindrome"
    
    # print(word[1:len(word)-1])
    return is_palindrome_3(word[1:len(word)-1])


# print(is_palindrome_3("Was it a car or a cat I saw?"))
# print(is_palindrome_3("Hdllo, World!H"))
