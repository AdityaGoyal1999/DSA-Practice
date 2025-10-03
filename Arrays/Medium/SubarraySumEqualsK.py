"""
Find nums of subarrays with sum equal to k.

nums = [1, 2, 3, 4, 5] 
k = 3 -> 2 [1, 2], [3]
"""

def getSubarraysSumK(nums: list, k: int) -> int:
    subarrays = {0: 1}
    runningSum = 0
    result = 0

    for num in nums:
        runningSum += num
        if runningSum - k in subarrays:
            result += subarrays[runningSum - k]
        
        if runningSum not in subarrays:
            subarrays[runningSum] = 1
        else:
            subarrays[runningSum] += 1
    
    return result

nums = [1, 2, 3, 4, 5]
k = 3
print(getSubarraysSumK(nums, k))