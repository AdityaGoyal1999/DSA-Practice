"""
Best time to buy and sell stocks. Return the maximum profit that can be made.

[7,1,5,3,6,4] → 5

Solution:
- Keep track of min and max of stock as you keep progressing.
"""

def stockMaxProfit(nums: list) -> int:
    if len(nums) <= 1:
        return 0
    
    minVal = nums[0]
    maxProfit = 0

    for num in nums:
        currProfit = num - minVal
        maxProfit = max(maxProfit, currProfit)

        minVal = min(minVal, num)
    
    return maxProfit

nums = [7, 1, 5, 3, 6, 4]
print(stockMaxProfit(nums) == 5)