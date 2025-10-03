"""
Binary Search in a rotated sorted array.

arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
key = 3

Solution
- Try to find continous patches that will influence your decision
"""

# O(log n)
# O(1)
def binarySearch(nums: list, key: int) -> bool:

    n = len(nums)
    b, e = 0, n-1

    while b <= e:
        m = (b + e) // 2
        if nums[m] == key:
            return True
        
        if nums[m] <= nums[e]:
            if nums[e] >= key > nums[m]:
                b = m + 1
            else:
                e = m - 1
        else:
            if nums[b] <= key < nums[m]:
                e = m - 1
            else:
                b = m + 1
    return False

nums = [5, 6, 7, 8, 9, 10, 1, 2, 3]
key = 3
print(binarySearch(nums, key))


# Test cases
test_cases = [
    ([5, 6, 7, 8, 9, 10, 1, 2, 3], 3),  # Should find 3
    ([5, 6, 7, 8, 9, 10, 1, 2, 3], 7),  # Should find 7
    ([5, 6, 7, 8, 9, 10, 1, 2, 3], 4),  # Should not find 4
    ([4, 5, 6, 7, 0, 1, 2], 0),         # Should find 0
    ([4, 5, 6, 7, 0, 1, 2], 3),         # Should not find 3
    ([1], 1),                           # Single element, should find
    ([1], 0),                           # Single element, should not find
]

print("Testing binary search in rotated array:")
for nums, key in test_cases:
    result = binarySearch(nums, key)
    print(f"Array: {nums}, Key: {key} -> Found: {result}")
