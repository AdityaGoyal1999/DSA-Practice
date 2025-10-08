"""
Count the vowels and consonants.

Solution - Iteration and checking each character.
"""

# O(n)
# O(1)
def countVowelsConsonants(s: str) -> tuple:

    vowels = "aeiou"
    numVowels, numCons = 0, 0

    for c in s:
        if c in vowels:
            numVowels += 1
        else:
            numCons += 1
    
    return (numVowels, numCons)


s = "hello"
print(countVowelsConsonants(s) == (2, 3))