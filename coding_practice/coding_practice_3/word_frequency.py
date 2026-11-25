from collections import defaultdict


def word_frequency(string: str):
    counter = defaultdict(int)
    
    for word in string.lower().split():
        counter[word] += 1
    
    num = 0

    for key, value in counter.items():
        if value > num:
           word, num = key, value
    
    return word   # type: ignore


print(word_frequency("Python is fun, and python is powerful"))
