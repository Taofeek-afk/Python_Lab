def self_split(string: str, sep=""):
    new_list: list = []
    substring: str = ""

    if not sep:
        for n in range(len(string)):
            if string[n] == " ":
                if substring:
                    new_list.append(substring)
                    substring = ""
            else:
                substring += string[n]

        if substring:
            new_list.append(substring)

        return new_list

    n: int = 0

    while n <= len(string) - len(sep):

        if string[n:n + len(sep)] == sep:
            new_list.append(substring)
            substring = ""
            n += len(sep)
        else:
            substring += string[n]
            n += 1

    # Add any characters remaining after the last possible
    # separator position.
    substring += string[n:]
    print(string[n:])

    new_list.append(substring)

    return new_list


print(self_split("apple banana ba arr", "a"))


result = "apple banana ba arr".split("a")  # noqa: SIM905
print(result)
# print(len(result[1]))