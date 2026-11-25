from collections import defaultdict


def word_frequency(string: str):
    count = defaultdict(int)

    for char in string.lower().split():
        count[char] += 1
    
    return count


print(word_frequency("python is fun and python is powerful"))
