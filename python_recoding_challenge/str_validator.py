# Concept: Dual-pointer branching recursion over three strings simultaneously.
# Problem
# Write a recursive function is_interleave(s1, s2, s3, i=0, j=0) that returns True if s3 is formed by an interleaving of s1 and s2, while preserving the relative left-to-right character order of both strings. Characters from both strings may be combined in different positions, but their original order within each individual string must remain unchanged.
# Examples
# Input:   s1 = "abc", s2 = "def", s3 = "adbcef"
# Output:  True

# Input:   s1 = "aab", s2 = "axy", s3 = "aaxaby"
# Output:  True

# Input:   s1 = "abc", s2 = "def", s3 = "abdfec"
# Output:  False

# Hints
# Use i to track the current position in s1.
# Use j to track the current position in s2.
# Derive the current position in s3 using k = i + j.
# Compare the current character in s3 with the current character in either s1 or s2.
# If the characters match, recursively explore that choice; if both choices are possible, explore both branches.
# Ensure all three strings are completely consumed.
# Constraints
# Zero for or while loops.
# Zero string slicing (for example, s[1:]).
# Zero new string concatenations.
# Compare characters using integer indices (i, j, and the derived k).
# Do not create additional strings.
# Preserve the original character order of both input strings.
# Do not hardcode the answers.
# What this tests: Dual-pointer recursion, recursive branching, index management, string comparison, Boolean logic, and simultaneous processing of multiple strings.

def is_interleave(s1, s2, s3, i=0, j=0):
    # if i+j == len(s3):
    #     return True
    
    if s1[i] == s3[i+j]:
        return is_interleave(s1, s2, s3, i+1, j)
    elif s2[j] == s3[i+j]:
        return is_interleave(s1, s2, s3, i, j+1)
    else:
        return False



print(is_interleave(s1 = "abc", s2 = "def", s3 = "adbcef"))

# Input:   s1 = "abc", s2 = "def", s3 = "adbcef"
# Output:  True

# Input:   s1 = "aab", s2 = "axy", s3 = "aaxaby"
# Output:  True

# Input:   s1 = "abc", s2 = "def", s3 = "abdfec"
# Output:  False