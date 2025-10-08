"""
Convert a string to an integer.

Explanation: Parse with sign and bounds.
Example: '-42' → -42
"""

def stringToInt(s: str) -> int:

    sign = 1
    numStr = ""

    if s[0] == "-":
        sign = -1
        numStr = s[1:]
    elif s[0] == "+":
        numStr = s[1:]
    else:
        numStr = s

    # Can also have a dictionary since we know where the number starts from.
    
    return sign * int(numStr)

print(stringToInt("-42") == -42)
print(stringToInt("0") == 0)