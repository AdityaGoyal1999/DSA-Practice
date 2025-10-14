"""
Find the length of the longest substring without repeating characters.

"abcabb" -> 3
"""

def longestRepeating(s: str) -> int:

    chars = set()
    l, r = 0, 0
    maxLen = 0

    while r < len(s):
        if s[r] in chars:
            while True:
                chars.remove(s[l])
                if s[l] == s[r]:
                    l += 1
                    break
                l += 1
            
        
        chars.add(s[r])
        r += 1

        length = r - l
        maxLen = max(maxLen, length)
    
    return maxLen


def longestRepeatingDict(s: str) -> int:

    freq = {}
    maxLen = 0
    l, r = 0, 0

    while r < len(s):
        if s[r] in freq and freq[s[r]] >= 1:
            while freq[s[r]] > 0:
                freq[s[l]] -= 1
                l += 1

        if s[r] in freq:
            freq[s[r]] += 1
        else:
            freq[s[r]] = 1
        r += 1

        maxLen = max(maxLen, r - l)

    return maxLen



s = "abcabb"
print(longestRepeatingDict(s))

s = "abcde"
print(longestRepeatingDict(s))

s = "aaa"
print(longestRepeatingDict(s))