#  Check for occuring chracters in two sorted given string "Hello and World", no duplicates, and it's lowercase insensitive

hello = "Hello"
world = "world"
contain_intersection = ""

for char in hello.lower():
    if char in world.lower() and char not in contain_intersection.lower():
        contain_intersection = contain_intersection + char


print(contain_intersection)


#  Write a program that returns the diff of two strings each and their intersection. 
string_1 = "Anderlechtt is a city in the netherlands"
string_2 = "string_1 contains an incorrect statement"

intersection = ""
diff_in_string_1_to_2 = ""
diff_in_string_2_to_1 = ""
duplicate = False
does_exist = False

#  Unpythonic Python
# Tracking states  | Tools = [True, False, None, continue, break, not]
for char in range(len(string_1)):
    for c in range(len(string_2)):
        if string_1[char] == string_2[c]:  # string_1 = parent variable  # Hold memory
            for i in range(len(intersection)):
                if string_1[char] == intersection[i]:
                    duplicate = True
            if duplicate == False:
                intersection = intersection + string_1[char]
            duplicate = False


for c in range(len(string_1)):
    for v in range(len(intersection)):
        if string_1[c] == intersection[v]:
            duplicate = True
    for i in range(len(diff_in_string_1_to_2)):
        if string_1[c] == diff_in_string_1_to_2[i]:
            does_exist = True
    if not duplicate and not does_exist:
        diff_in_string_1_to_2 += string_1[c]
    duplicate = False
    does_exist = False


for c in range(len(string_2)):
    for v in range(len(intersection)):
        if string_2[c] == intersection[v]:
            duplicate = True
    for i in range(len(diff_in_string_2_to_1)):
        if string_2[c] == diff_in_string_2_to_1[i]:
            does_exist = True
    if not duplicate and not does_exist:
        diff_in_string_2_to_1 += string_2[c]
    duplicate = False
    does_exist = False



print(
    f"what both strings has in common: '{intersection}'", 
    f"What string_1 has that string_2 does not: '{diff_in_string_1_to_2}'",
    f"What string_2 has that string_1  does not: '{diff_in_string_2_to_1}'", sep="\n")
