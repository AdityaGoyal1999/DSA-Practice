"""
Check if the string provided with only brackets are balanced.

{[()]} → True

Solution:
- Use stack. Check when popping 
"""

def areBracketsBalanced(s: str) -> bool:
    brackets = {
        "}" : "{",
        ")": "(",
        "]": "["
    }

    stack = []

    for bracket in s:
        if bracket not in brackets:
            stack.append(bracket)
        else:
            if stack[-1] != brackets[bracket]:
                return False
            else:
                stack.pop()
    
    return len(stack) == 0


print(areBracketsBalanced("()"))
print(areBracketsBalanced("({[]})"))
print(areBracketsBalanced("()[]{}"))
print(areBracketsBalanced("(]") == False)