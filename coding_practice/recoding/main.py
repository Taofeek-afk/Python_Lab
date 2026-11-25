def compress_string(word):
    if not word:
        return ""
    
    count = 1
    result = ""

    for n in range(1, len(word)):
        if word[n-1] == word[n]:
            count += 1
        else:
            result += word[n-1] + str(count)
            count = 1
            
    result += word[-1] + str(count) # type: ignore
            
    return result



# print(compress_string("appaaba"))


# # count every char met, append to result if the next char is different from the previous char

# if char not equal prev char, append to result with count, else count = 1

def longest_unique_substring(word):
    lexicon = {}
    container = ""
    items = []
    # steps = 0
    # count = 0
    
    for n in range(1, len(word)):
        
        for j in range(n):
            if word[j] == word[n]:
                items.append(container)
                container = ""
                break
            else:
                container += word[j]  

    return lexicon


# count as long as there is no non-repeating characters in the accumulated container, else, wrap up and keep the count.
# # print(longest_unique_substring(""))
# print(longest_unique_substring("abcabcbb"))
# # "abc"

# print(longest_unique_substring("bbbbb"))
# # # "b"

# print(longest_unique_substring("pwwkew"))
# # # "wke"

# print(longest_unique_substring("abcdef"))
# # "abcdef"


def group_anagrams(words):
    ...
    
words = [
    "eat",
    "tea",
    "tan",
    "ate",
    "nat",
    "bat"
]

group_anagrams(words)


def merge_intervals(intervals):
    ...
    
    
merge_intervals([
    [1, 3],
    [2, 6],
    [8, 10],
    [9, 12]
])


# [
#     [1, 6],
#     [8, 12]
# ]

sizes = ["S", "M", "L"]
colors = ["black", "white", "brown"]

tshirts = ((color, size) for color in colors for size in sizes)

# print(next(tshirts))
# print(next(tshirts))
# print(next(tshirts))
# print(next(tshirts))
# print(next(tshirts))
# print(next(tshirts))

# items = [item for item in tshirts]
# print(items)

# try:
#     print(next(tshirts))
# except StopIteration:
#     print("\nEnd of sequence")

# If the generator obj doesn't keep items in memory then is it basically for streaming large external files?? or remodifying an existing large file to minimize space usage?? How does %s/%s work in Python, as in (for passport in travelers_id: print("%s/%s" % passport))


travelers_id = [("USA", "31195855"), ("BRA", "CE342567"), ("ESP", "XDA205856")]

# for passport in travelers_id:
#     print("{}/{}".format(*passport))

def check_scope():
    a = 5
    b = "hello"
    print(locals())  # Output: {'a': 5, 'b': 'hello'}
    
    # Trying to modify it fails:
    locals()['a'] = 99 
    print(a)  # Output: 5 (It didn't change!)

check_scope()
print(locals())
