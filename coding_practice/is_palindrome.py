def is_palindrome(string: str): # Two pointer 7.0
    if not string:
        return True
    
    i = 0
    j = 1
    
    mid = len(string) // 2
    
    while i < mid:
        if string[i] != string[len(string)-j]:
            return False

        i += 1
        j += 1
    
    return True


print(is_palindrome("racecar"))


def is_palindrome_checker(word: str):
    left, right = 0, len(word) - 1
    
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    
    return True

print(is_palindrome_checker("apple"))
