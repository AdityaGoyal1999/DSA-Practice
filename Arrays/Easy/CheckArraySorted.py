"""
Check if the array is sorted.

nums = [1, 2, 3, 4, 5] -> True

Solution 
- One pass comparing adjacent elements
"""

def isArraySorted(nums: list) -> bool:
    
    n = len(nums)
    for i in range(1, n):
        if nums[i] < nums[i-1]:
            return False
    
    return True

nums = [1, 2, 3, 4, 5]
print(isArraySorted(nums))

nums = [1, 2, 3, 5, 4]
print(isArraySorted(nums))