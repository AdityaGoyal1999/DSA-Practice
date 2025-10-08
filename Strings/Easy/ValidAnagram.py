"""
Valid Anagram

Anagram - if 2 strings can be rearranged to each other.

Solution:
- Compare the frequency of strings.
"""

def getCharFreq(s) -> dict:
    freq = {}
    for c in s:
        if c not in freq:
            freq[c] = 1
        else:
            freq[c] += 1
    return freq

# O(n)
# O(1)
def isAnagram(s1: str, s2: str) -> bool:

    if len(s1) != len(s2):
        return False
    
    s1_freq = getCharFreq(s1)
    s2_freq = getCharFreq(s2)
    
    for c in s1_freq:
        if c not in s2_freq or s1_freq[c] != s2_freq[c]:
            return False
    
    
    return True

s1 = "anagram"
s2 = "nagaram"
print(isAnagram(s1, s2) == True)