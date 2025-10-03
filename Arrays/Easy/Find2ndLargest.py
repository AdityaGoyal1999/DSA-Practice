"""
Find the second largest element in the array.

[2, 3, 1, 5, 4] -> 5
Solution: Get largest and 2ndLargest in 1 pass.
"""
# TODO: revise again - made a mistake here

def findSecondLargest(nums: list) -> int:
    # constraints: len(nums) > 1

    largest, prev_largest = float("-inf"), float("-inf")

    for num in nums:
        if num > largest:
            prev_largest = largest
            largest = num
        elif num > prev_largest:
            prev_largest = num
    
    return prev_largest
    


nums = [2, 3, 1, 5, 4] 
print(findSecondLargest(nums))

