"""
Rotate the array by k steps.

nums = [1, 2, 3, 4, 5] 
k = 3

Solution: 
- Reversal
    - Reverse the array
    - Reverse first half and second half of the array then

- TODO: Checkout modular index write solution
"""

def reverseSegment(nums, start, end):
    i = start
    j = end

    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1

def rotateArray(nums: list, k: int) -> list:
    
    # reverse whole array
    n = len(nums)
    reverseSegment(nums, 0, n-1)

    # reverse first half
    reverseSegment(nums, 0, k-1)

    # reverse second half
    reverseSegment(nums, k, n-1)

    return nums


nums = [1, 2, 3, 4, 5]
k = 3

print(rotateArray(nums, k))

nums = [1, 2, 3, 4, 5]
k = 5

print(rotateArray(nums, k))
