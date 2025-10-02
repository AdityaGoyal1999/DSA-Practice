"""
Implement a program to perform linear search on an array.
"""

# O(n)
# O(1)
def linearSearch(arr: list, val: int) -> bool:
    
    for num in arr:
        if num == val:
            return True
    
    return False


arr = [1, 2, 3, 4, 5, 6, 7]
print(linearSearch(arr, 6))
print(linearSearch(arr, 9))