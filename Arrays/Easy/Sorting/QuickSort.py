"""
Implement quick sort algorithm

Take a pivot. Divide and conquer algorithm.
"""
# TODO: Do in-place and make it faster

# O(n^2) worst case - O(n log n) average case
# O(n log n) space complexity
def quicksort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left_half = []
        right_half  = []

        for num in arr[1:]:
            if num < pivot:
                left_half.append(num)
            else:
                right_half.append(num)
        
        left_sorted = quicksort(left_half)
        right_sorted = quicksort(right_half)

        return left_sorted + [pivot] + right_sorted


arr = [-1, 5, 6, 2, 1, 3]
print(quicksort(arr))