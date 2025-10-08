"""
Reverse the words in the string.

'the sky is blue' → 'blue is sky the'

Solution:
- Extract words and reverse them.
"""

# O(n)
# O(n)
def reverseWords(s: str) -> str:

    words = s.split(' ')
    return ' '.join(words[::-1])

s = "the sky is blue"
print(reverseWords(s))