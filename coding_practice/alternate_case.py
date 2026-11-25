def alternate_case(string: str):
    # alternated_string = ""
    container = []
    for char in string:
        if char.isupper():
            # alternated_string += char.lower()
            container.append(char.lower())
            # print(alternated_string)
        elif char.islower():
            # print(alternated_string, "else runs here")
            # alternated_string += char.upper()
            container.append(char.upper())
        else:
            # alternated_string += char
            container.append(char)
    
    return "".join(container)

# print(ord("z")) # A = 65, Z = 90. a = 97, z = 122


def alternate_case_2(string: str):
    container = ""
    for n in range(len(string)):
        if string[n] >= "A" and string[n] <= "Z":
            container += chr(ord(string[n]) + 32) 
        elif string[n] >= "a" and string[n] <= "z":
            container += chr(ord(string[n]) - 32)
        else:
            container += string[n]
    
    return container


# print(alternate_case_2("upper_case, LOWER_CASE"))

# word = input("Provide a word: ")
alternated_string_3 =  lambda word: "".join([x.lower() if x.isupper() else x.upper() if x.islower() else x for x in word])

# print(alternated_string_3(word))


# def alternate_string_4(string):
#     return "".join([x.swapcase() for x in string]) or string.swapcase()

# print(alternate_string_4("to_upper_case, TO_LOWER_CASE"))


print("upper_case 999 to LOWER_CASE".swapcase())
