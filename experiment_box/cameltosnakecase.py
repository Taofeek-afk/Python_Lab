#  Write a function that converts a string from camelCase to snake_case. 
# If the string is empty, return an empty string. ;
# If the string is not camelcase return the string unchanged. ;
# If the string is camelcase return the snake_version of the string
#  camelCase, CamelCase
# Implementing Go style. # A is 65, Z is 90. a is 97, z is 122
#  Tracking states  | Tools = [True, False, None, continue, break, not, len]


def check_if_camel_to_snake_case(string: str):
    if string == "":
        return ""

    snake_case = ""

    for char in range(len(string)):
        # Return unchanged if a character is not a letter.
        if not (65 <= ord(string[char]) <= 90) and not (97 <= ord(string[char]) <= 122):
            return string

        # Return unchanged if two consecutive uppercase letters are found.
        if char + 1 < len(string) and 65 <= ord(string[char]) <= 90:
                return string

        if snake_case != "" and (65 <= ord(string[char]) <= 90):
            snake_case += "_"
            snake_case += chr(ord(string[char])+32)
            continue

        snake_case += chr(ord(string[char]))

    return snake_case


print(check_if_camel_to_snake_case("AnOrange"))
