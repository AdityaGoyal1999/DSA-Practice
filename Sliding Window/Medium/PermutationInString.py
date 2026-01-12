"""
Given two strings, check if one is a permutation of the other.

"abc" -> "bca" -> True
"abc" -> "def" -> False
"""

def getCharFreq(s: str) -> dict:
    freq = {}
    for c in s:
        if c not in freq:
            freq[c] = 1
        else:
            freq[c] += 1
    return freq

def compareFreqs(freq1: dict, freq2: dict) -> bool:
    for c in freq1:
        if c not in freq2 or freq1[c] != freq2[c]:
            return False
    return True

def isPermutation(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False
    
    s1_freq = getCharFreq(s1)
    s2_freq = getCharFreq(s2[:len(s1)])

    if s1_freq == s2_freq:
        return True
    
    if compareFreqs(s1_freq, s2_freq):
        return True
    
    l, r = 0, len(s1)
    while r < len(s2):
        if s[r] in s2_freq:
            s2_freq[s[r]] += 1
        else:
            s2_freq[s[r]] = 1
        
        s2_freq[s2[l]] -= 1
        l += 1
        r += 1

        if compareFreqs(s1_freq, s2_freq):
            return True
        
    return False

s1 = "abc"
s2 = "bca"
print(isPermutation(s1, s2))
s1 = "abc"
s2 = "def"
print(isPermutation(s1, s2))