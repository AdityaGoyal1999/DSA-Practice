"""
Group the anagrams.

['eat','tea','tan','ate','nat','bat'] → [['eat', 'tea', 'ate], ['tan', 'nat'], ['bat']]
"""


# O(nslogs)
# O(ns)
def groupAnagrams(strings: list) -> list:

    # sort the strings and then put them in a dictionary 
    anagrams = {}
    for s in strings:
        s_sorted = ''.join(sorted(s))
        if s_sorted in anagrams:
            anagrams[s_sorted].append(s)
        else:
            anagrams[s_sorted] = [s]

    # extract the answer
    result = []
    for anagram in anagrams:
        result.append(anagrams[anagram])
    
    return result

strings = ['eat','tea','tan','ate','nat','bat']
print(groupAnagrams(strings))