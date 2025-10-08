"""
Create a naive string searching algorithm. Given a string and substring, see if it exists.

Solution:
- O(n * m) 
- Nested loops
"""

# O(n * m)
# O(1)
def strPatternMatching(string: str, subString: str) -> int:

    n = len(string)
    m = len(subString)

    for i in range(n - m + 1):

        j = i

        while j-i < len(subString) and string[j] == subString[j - i]:
            j += 1
        
        if j - i == len(subString):
            return i
    
    return -1

string = "aditya"
subString = "ya"
print(strPatternMatching(string, subString))

string = "hello"
subString = "l"
print(strPatternMatching(string, subString))