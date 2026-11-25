def run_encoding_length(text: str):
    res = ""
    text = text.strip()
    sample = list(text)
    sample_2 = list.copy(sample)
    print("Sample 2: ", sample_2)
    print(sample)
    
    # for ch in text:
    #     sample.append(ch)
    
    res = []
    
    for item in sample:
        if len(res) == 0:
            res.append(item)
            res.append(1)
        elif item == res[-2]:
            res[-1] += 1
        elif res[-2] != item:
            res.append(item)
            res.append(1)
        
    result = ""
    
    for item in res:
        if type(item) == str:
            result += item
        else:
            result += str(item)
    
    return result


test = "abgfraa"

print(run_encoding_length(test))