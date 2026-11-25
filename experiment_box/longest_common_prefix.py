# # def longestCommonPrefix(strs: list[str]) -> str:
# #         if not strs:
# #             return ""

# #         first = strs[0]

# #         for i in range(len(first)):
# #             char = first[i]
# #             for string in strs[1:]:
# #                 # If we reach the end of any string OR characters don't match
# #                 if i == len(string) or string[i] != char:
# #                     return first[:i]

# #         return first

# # print(longestCommonPrefix(["flower", "flown", "fbread"]))

def valid_parentheses(string: str):
    opening_brackets = {"(": 1, "{": 1, "[": 1,}
    closing_brackets = {")": -1, "}": -1, "]": -1}
    count = 0
    num = len(string)
    
    


# print(valid_parentheses(")("))
        
# # Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# # An input string is valid if:

# #     Open brackets must be closed by the same type of brackets.
# #     Open brackets must be closed in the correct order.
# #     Every close bracket has a corresponding open bracket of the same type.
