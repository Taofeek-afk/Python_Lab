text_1 = "(a + b) * [c - d]"
text_2 = "(a + b)]"
text_3 = "[(a + b) * {c - d}]"


def balanced_parentheses(input: str = text_3) -> str:
    stack = []
    parentheses = {")":"(", "}":"{", "]":"["}
    brackets = "({["
    
    for i, n in enumerate(input):
    
        if n in brackets:
            stack.append(n)

            if len(stack) > 1 and stack[i-1] == stack[i]:
                return "Not balanced (unclosed)"
            elif len(stack) > 1 and stack[i-1] in brackets:
                return "Not balanced (wrong order)"

        elif n in parentheses:
            if not stack:
                return "Not balanced (mismatched type)"
            
            value = stack.pop()
        
            if value != parentheses[n]:
                return "Not balanced"
    
    if stack:
        return "Not balanced"
    
    return "Balanced"


# print(balanced_parentheses("([)]"))


def balanced_parentheses_2(text):
    parentheses = {")":"(", "}":"{", "]":"["}
    stack = []
    
    for n in text:
        if n in parentheses.values():
            stack.append(n)
        elif n in parentheses and (not stack or stack.pop() != parentheses[n]):
            return "Not balanced"

    return "Not balanced" if stack else "Balanced"
