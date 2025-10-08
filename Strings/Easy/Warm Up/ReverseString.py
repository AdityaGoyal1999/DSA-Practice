"""
Reverse a string
"""

# O(n)
# O(n)
def reverseString(s: str) -> str:

    chars = [''] * len(s)

    i = 0
    for i in range(len(s)):
        chars[len(s) - i - 1] = s[i]
    
    return ''.join(chars)


print(reverseString("hello"))