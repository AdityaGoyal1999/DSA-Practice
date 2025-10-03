"""
Find the Min and Max element in the array.

Solution -
- One pass scan should do the job.
"""

def getMinMax(nums: list) -> tuple:

    smallest = float("inf")
    largest = float("-inf")

    for num in nums:
        smallest = min(smallest, num)
        largest = max(largest, num)
    
    return smallest, largest

nums = [1, 2, 3, 4, 5, -100]
print(getMinMax(nums))
