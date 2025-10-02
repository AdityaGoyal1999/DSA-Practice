"""
Implement bubble sort

Swapping the adjacent elements and putting them at the end.
"""


def bubbleSort(arr: list) -> list:

    n = len(arr)

    for i in range(n):
        for j in range(1, n - i):

            if arr[j - 1] > arr[j]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

    return arr 


arr = [5, 4, 3, 2, 1]

print(bubbleSort(arr))
