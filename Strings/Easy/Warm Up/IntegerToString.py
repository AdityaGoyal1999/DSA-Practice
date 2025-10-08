"""
Convert an integer to string.

Soltution:
- Extract digits and store them in a list
- later create a string from the list

Be careful of the sign
"""

# O(log n)
# O(n)
def integerToString(num: int) -> str:

    sign = 1
    if num < 0:
        sign = -1
    result = []
    
    while num > 0:
        result.append(str(num % 10))
        num = num // 10
    
    return ''.join(result[::-1])

print(integerToString(1123) == "1123")