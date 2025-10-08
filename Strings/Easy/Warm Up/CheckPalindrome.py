"""
Check if a string is palindrome.
"""

def checkPalindrome(s: str) -> bool:
    # ignoring whitespaces
    # case insensitive

    i = 0
    j = len(s) - 1

    while i < j:
        if s[i].isalnum() and s[j].isalnum():
            if s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        else:
            if not s[i].isalnum():
                i += 1
            if not s[j].isalnum():
                j -= 1
    
    return True


print(checkPalindrome("hello") == False)
print(checkPalindrome("RACE car") == True)