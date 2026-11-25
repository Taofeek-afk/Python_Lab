# Problem
# Write a recursive function word_break(s, word_dict) that returns True if the string s can be segmented into a space-separated sequence of one or more words from word_dict. Otherwise, return False. You may reuse dictionary words multiple times.
# Examples
# Input:   s = "leetcode", word_dict = ["leet", "code"]
# Output:  True

# Input:   s = "applepenapple", word_dict = ["apple", "pen"]
# Output:  True

# Input:   s = "catsandog", word_dict = ["cats", "dog", "sand", "and", "cat"]
# Output:  False

# Hints
# Base Case: If s is an empty string (""), return True.
# Try different prefixes of the string to determine whether they exist in the dictionary.
# If a prefix matches a dictionary word, recursively check the remaining substring.
# Consider using memoization to avoid repeatedly solving the same subproblems.
# Constraints
# Use recursion to solve the problem.
# Dictionary words can be reused multiple times.
# Handle cases where no valid segmentation exists.
# Do not hardcode the answers.
# Use memoization where necessary to avoid redundant recursive calculations.
# What this tests: Recursive branching, base cases, string slicing, dictionary lookup, memoization, and decision-tree problem-solving


def truncate(word, target):
    for n in range(len(word)):
        if word[n:len(target)+n] == target:
            word = word[:n] + word[len(target)+n:]
    
    return word

print(truncate("appleapp", "app"))

def word_break(s, word_dict):
    if not s:
        return True
    
    if word_dict[0] in s:
        s = truncate(s, word_dict[0])
    else:
        return False
    
    return word_break(s, word_dict[1:])


print(word_break(s="leetcode", word_dict=["leet", "code"]))
print(word_break(s = "applepenapple", word_dict = ["apple", "pen"]))
print(word_break(s = "catsandog", word_dict = ["cats", "dog", "sand", "and", "cat"]))
