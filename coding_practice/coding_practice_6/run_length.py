def run_length_encoding(string: str):
    
    string += "_"
    compressed = ""
    
    count = 1
    for n in range(len(string)-1):
        if string[n] != string[n+1]:
            compressed += string[n] + str(count)
            count = 1
        else:
            count += 1
    
    return compressed


# print(run_length_encoding("aabbaa"))


def run_length_encoding_2(string: str):
    if len(string) == 1:
        result = string[0] + "1"
        return result
    
    compressed = ""
    count = 1
    
    for n in range(1, len(string)):
        if string[n-1] != string[n]:
            compressed += string[n-1] + str(count)
            count = 1
        else:
            count += 1

    compressed += string[n] + str(count) # type: ignore
    
    return compressed


# print(run_length_encoding_2("aabbaa"))               


def run_length_decoding(encoded_str: str) -> str:
    if len(encoded_str) < 2 or len(encoded_str) % 2 != 0:
        return "Invalid input"
    
    res = ""

    for n in range(0, len(encoded_str), 2):
        if not str.isalpha(encoded_str[n]) or not str.isdigit(encoded_str[n+1]):
            return "Wrong encoding format"

        res += encoded_str[n] * int(encoded_str[n+1])
    
    return res


# print(str.isupper("apple"))
