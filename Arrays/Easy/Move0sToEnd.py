"""
Move all the 0s to the end.

[1, 2, 0, 2, 0, 1] -> [1, 2, 2, 1, 0, 0]
"""

# O(n)
# O(1)
def move0s(arr: list) -> list:
    i = 0
    j = len(arr) - 1

    while i < j:
        if arr[i] == 0:
            arr[j], arr[i] = arr[i], arr[j]
            j -= 1
        else:
            i += 1
    
    return arr

nums = [1, 2, 0, 2, 0, 1]
print(move0s(nums))