"""
Reverse a string with a stack.

Solution:
- Keep pushing characters in a stack
- Pop the characters and they'll be in reversed order
"""
from StackImplementation import Stack

# O(n)
# O(n)
def reverseString(s: str) -> str:
    
    stack = Stack([])
    result = []

    for c in s:
        stack.push(c)
    
    while len(stack) > 0:
        result.append(stack.pop())

    return ''.join(result)

s = "hello"
print(reverseString(s) == "olleh")

