def is_palindrome():
    word = input("provide a word: ")
    
    left = 0
    right = len(word) - 1
    
    mid = len(word) // 2
    
    while left <= mid:
        # print(left, right)
        if word[left] != word[right]:
            return "Not a palindrome"
        
        left += 1
        right -= 1
        
    return "Palindrome"

print(is_palindrome())