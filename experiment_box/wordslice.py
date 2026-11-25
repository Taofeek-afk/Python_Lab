def first_word(string: str) -> str:
    if string == "":
        return string

    for index, char in enumerate(string):
        if char == " ":
            return string[:index]


print(first_word("Remember Red, Hope is a good thing, and no good thing ever dies"))


def last_word(string: str) -> str:
    if string == "":
        return ""

    container = ""
    result = ""

    for char in string:
        if char == " ":
            if container != "":
                result = container
            container = ""
            continue
        container += char

    if container != "":
        result = container

    return result


print(last_word("    Remember Red, Hope is a good thing, and no good thing ever dies       "))


#  Write a function called RepeatAlpha that takes a string and displays it repeating each alphabetical characters as many many times as it alphabetical index
def repeat_alpha(string: str) -> str:
    container = ""
    count = 1

    for char in string:
        container += char * count
        count += 1

    return container


print(repeat_alpha("abhgic"))
