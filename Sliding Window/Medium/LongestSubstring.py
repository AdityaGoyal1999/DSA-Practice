"""
Find the length of the longest substring without repeating characters.

"abcabcbb" -> 3
"""

def longestSubstring(s: str) -> int:
    l, r = 0, 0
    maxLength = 0
    chars = set()

    while r < len(s):
        while s[r] in chars:
            chars.remove(s[l])
            l += 1
        
        chars.add(s[r])
        r += 1

        maxLength = max(maxLength, r - l)
    
    return maxLength

s = "abcabcbb"
print(longestSubstring(s) == 3)
s = "bbbbb"
print(longestSubstring(s) == 1)
s = "pwwkew"
print(longestSubstring(s) == 3)