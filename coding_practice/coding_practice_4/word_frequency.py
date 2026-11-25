# def count_words(words: list[str]):
#     word_count = {}
#     _ = [word_count[word] = word_count.get(word, 0) + 1 for word in words]
#     print(_)
    
    

def count_words(words: str):
    words = words.lower().split() # pyright: ignore[reportAssignmentType]
    word_count = {}
    
    for word in words:
        word_count[word.lower()] = word_count.get(word.lower(), 0) + 1
    
    return word_count


wordss = "Python is fun and python is powerful"
print(count_words(wordss))


def most_frequent(words):
    words = count_words(words)
    most_occurred = ""
    highest = 0
    
    for key, value in words.items():
        print(key, value)
        if value > highest:
            highest = value
            most_occurred = key
        
    return most_occurred
    

print(most_frequent(wordss))
