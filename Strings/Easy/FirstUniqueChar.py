"""
Find the index of the first unique character in a string that appears only once.

Solution
- Get freq of characters
- Parse again and see whichever has just 1 char
"""

# O(n)
# O(1)
def firstUnique(s: str) -> int:

    freq = {}
    for c in s:
        if c not in freq:
            freq[c] = 1
        else:
            freq[c] += 1
    
    for i in range(len(s)):
        c = s[i]
        if freq[c] == 1:
            return i
    
    return -1

s = "hhh"
print(firstUnique(s) == -1)

s = "leetcode"
print(firstUnique(s) == 0)