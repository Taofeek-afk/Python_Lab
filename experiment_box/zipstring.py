#  Write a function that takes a string
# and returns a new string that replaces every character with the number of duplicates
# and the character itself, deleting the extra duplication

def zipstring(string: str):
    
    found = ""
    count = 0
    
    for i in range(len(string)):
        if string[i] in found:
            continue
        for c in range(len(string)):
            if string[i] == string[c]:
                count += 1
        found += str(count)
        found += string[i]
        count = 0
    
    return found


print(zipstring("apple"))
    
    
# for j in range(len(string)):
#     if string[i] == string[j]:
#         count += 1

# gcc hello.c -o hello
# ./hello

# gcc -Wall -Wextra -std=c11 hello.c -o hello