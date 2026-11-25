def find_subset(haystack, needle):
    for i in range(len(haystack)):
        if haystack[i:len(needle)+i] == needle:
            return i
    return False


print(find_subset("intonation", "iona"))
