"""
Find the product of the array except itself.

[1, 2, 3, 4] -> [24, 12, 8, 6]
Solution
- Prefix and postfix sum in 2 iterations
"""

def arrayProduct(nums: list) -> list:

    n = len(nums)
    result = [1] * n

    prefix = nums[0]
    for i in range(1, n):
        result[i] *= prefix
        prefix *= nums[i]

    postfix = nums[n-1]
    for i in range(n-2, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]
    
    return result

nums = [1, 2, 3, 4]
print(arrayProduct(nums))