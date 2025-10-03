"""
Find the missing number in the range 0 to n. 

Can use XOR or sum of nums.
[0, 1, 3] -> []
"""


def findMissingNum(nums: list) -> int:

    actual_sum = sum(nums)

    n = len(nums)
    target_sum = (n * (n+1)) // 2

    return target_sum - actual_sum

def findMissingNumXOR(nums: list) -> int:

    running_xor = 0
    for num in nums:
        running_xor ^= num
    
    for num in range(0, len(nums)+1):
        running_xor ^= num
    
    return running_xor


nums = [0, 1, 3]
print(findMissingNumXOR(nums))


nums = [0, 1, 2]
print(findMissingNumXOR(nums))

nums = [1, 2, 3]
print(findMissingNumXOR(nums))