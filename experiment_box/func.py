def self_split(string:str, sep="", maxsplit: None | int = None):  # Work on empty input split
    new_list: list = []
    substring: str = ""
    
    if not sep:
    
        for n in range(len(string)):
            
            if string[n] == " " and substring:
                new_list.append(substring)
                substring: str = ""
                continue
            
            if string[n] != " ":
                substring += string[n]
        
        if substring:
            new_list.append(substring)
        
        return new_list
    
       
    n: int = 0
    length: int = len(string) - len(sep)
    
    while n <= length:

        if string[n: n+len(sep)] == sep:
            new_list.append(substring)
            substring: str = ""
            n += len(sep)
            
            if len(new_list) == maxsplit:
                break
            
        else: 
            substring += string[n]
            n += 1
            


    substring += string[n:]

    new_list.append(substring)  

    return new_list


print(self_split("apple   apple     apple apple", " ", maxsplit=2))


result = "apple   apple     apple apple".split(" ", maxsplit=2)  # noqa: SIM905
print(result)
# print(len(result[1]))
