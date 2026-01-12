"""
Given an array of prices, find the maximum profit that can be made by buying and selling the stock.

[7,1,5,3,6,4] -> 5
"""

def maxProfit(prices: list) -> int:
    maxProfit = 0
    minPrice = prices[0]

    for price in prices:
        maxProfit = max(maxProfit, price - minPrice)
        minPrice = min(minPrice, price)
    
    return maxProfit

prices = [7,1,5,3,6,4]
print(maxProfit(prices) == 5)