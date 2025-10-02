"""
Implement a program that performs binary search on a sorted array.

arr = [1, 2, 3, 4, 5, 6]
"""

def binarySearch(arr: list, val: int) -> bool:
    
    b, e = 0, len(arr) - 1
    
    while b <= e:
        m = (b + e) // 2
        if arr[m] == val:
            return True
        elif arr[m] > val:
            e = m - 1
        else:
            b = m + 1
    return False


arr = [1, 2, 3, 4, 5, 6, 7]

print(binarySearch(arr, 2))
print(binarySearch(arr, 10))