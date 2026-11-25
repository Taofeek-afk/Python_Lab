def anagram(string_1, string_2):
    if len(string_1) != len(string_2):
        return "Not an anagram"
    
    lexicon = {}
    lexicon_2 = {}

    for char in string_1:
        try:
            lexicon[char] += 1
        except KeyError:
            lexicon[char] = 1
            
    for char in string_2:
        try:
            lexicon_2[char] += 1
        except KeyError:
            lexicon_2[char] = 1
        
    if lexicon == lexicon_2:
        return "Anagram"
    
    return "Not an anagram"


print(anagram("trinaagle", "integrgal"))
