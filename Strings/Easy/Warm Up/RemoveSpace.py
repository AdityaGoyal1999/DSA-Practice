"""
Filter out the whitespace characters.
"""

# O(n)
# O(n)
def filterSpace(s: str) -> str:
    result = []

    for c in s:
        if c == " ":
            continue
        result.append(c)
    
    return ''.join(result)

s = "h  ello"
print(filterSpace(s) == "hello")


"""
Imperative that we use list.
If we were to modify the string, that would've given us

O(n^2) runtime
O(n) space
"""