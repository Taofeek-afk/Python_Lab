# Wildcard Pattern Matcher: Recursive String Matching
# Suggested time: 25 to 30 minutes
# Concept: Multi-branch string consumption using recursive pattern matching.
# Problem
# Write a recursive function is_match(text, pattern) that returns True if the pattern matches the entire text. The pattern supports two special wildcard characters:
# Input:   text = "cat", pattern = "c?t"
# Output:  True

# Input:   text = "dog", pattern = "d*g?"
# Output:  False

# Input:   text = "abc", pattern = "*"
# Output:  True

# Hints
# If the current pattern character is a normal character, compare it with the current text character.
# If the current pattern character is ?, it can match any single character.
# If the current pattern character is *, explore two possibilities: let * match zero characters and move to the next pattern character, or let * consume one text character and continue matching.
# Both the text and pattern must be completely matched for the result to be True.
# Constraints
# Zero for or while loops.
# Zero regular expressions (re).
# Do not use the in operator.
# Use recursion to explore matching possibilities.
# ? must match exactly one character.
# * must match zero or more characters.
# The entire text must match the entire pattern.
# Do not hardcode the answers.
# What this tests: Recursive branching, string matching, wildcard logic, base cases, character comparison, and multi-path decision-making.


def wild_card(text, pattern):
    if not text and not pattern:
        return True
    
    if not pattern:
        return False
    

    if pattern[0] == '*':
        match_zero = wild_card(text, pattern[1:])
        
        match_more = bool(text) and wild_card(text[1:], pattern)
        
        return match_zero or match_more
    
    if text and (text[0] == pattern[0] or pattern[0] == '?'):
        return wild_card(text[1:], pattern[1:])
    
    return False


# ? matches any single character.
# * matches zero or more characters.
# Examples
# Input:   text = "hello", pattern = "h*o"
# Output:  True