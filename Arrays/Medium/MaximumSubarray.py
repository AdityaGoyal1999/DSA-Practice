"""
Find the maximum subarray in a given array.

nums = [1, 2, 3, -7, 10, 4] -> 14

Solution - Kadane's algorithm
"""

def maximumSubarraySum(nums: list) -> int:
    maxSum = nums[0]
    runningSum = 0

    for num in nums:
        runningSum += num
        maxSum = max(maxSum, runningSum)

        if runningSum < 0:
            runningSum = 0
    
    return maxSum

        
nums = [1, 2, 3, -7, 10, 4]
print(maximumSubarraySum(nums))


def getMaximumSubarray(nums: list) -> list:
    maxSum = float("-inf")
    start = None
    end = None

    runningSum = 0

    for i in range(len(nums)):
        num = nums[i]
        runningSum += num

        if runningSum > maxSum:
            maxSum = runningSum
            end = i

        if runningSum <= 0:
            runningSum = 0
            start = i+1
        
    
    return nums[start: end+1]

nums = [1, 2, 3, -7, 10, 4, -4]
print(getMaximumSubarray(nums))