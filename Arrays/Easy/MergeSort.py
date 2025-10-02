"""
Implement merge sort algorithm.

Divide and conquer algorithm where we divide, sort the halves and merge.
"""

# TODO: Do it in-place and make it faster

def merge(arr1: list, arr2: list) -> list:
    arr = []

    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1
    
    arr.extend(arr1[i:])
    arr.extend(arr2[j:])

    return arr


# O(n log n)
# O(n log n)
def mergeSort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    
    else:
        mid = len(arr) // 2
        left_sorted = mergeSort(arr[:mid])
        right_sorted = mergeSort(arr[mid:])

        return merge(left_sorted, right_sorted)


arr = [5, 4, 3, 2, 1]
print(mergeSort(arr))