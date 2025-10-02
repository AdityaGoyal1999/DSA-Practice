"""
Implement Insertion Sort.

Insert each element into the sorted prefix.
"""

# O(n^2)
# O(1)
def insertionSort(arr: list) -> list:
    
    n = len(arr)

    # start from 2nd element as we consider 1st to be sorted

    for i in range(1, n):

        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = key
    
    return arr


arr = [5, 4, 3, 2, 1]
print(insertionSort(arr))