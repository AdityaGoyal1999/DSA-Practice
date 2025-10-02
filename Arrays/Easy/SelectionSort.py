"""
Implement selection sort

Select the minimum at each pass and place at front.
"""
def selectionSort(arr: list) -> list:
    
    n = len(arr)

    for i in range(n):
        smallest, smallest_i = float("inf"), i

        for j in range(i, n):

            if arr[j] < smallest:
                smallest = arr[j]
                smallest_i = j
        
        arr[smallest_i], arr[i] = arr[i], arr[smallest_i]

    return arr

arr = [5, 4, 3, 2, 1]
print(selectionSort(arr))

