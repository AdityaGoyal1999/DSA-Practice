"""
Given an array of numbers, get the length of the longest consecutive sequence.

[1, 2, 3, 4, 100, 200] -> 4
"""

def findLongestConSeq(nums: list) -> int:
    
    num_set = set(nums)

    global_len = 0

    for num in num_set:
        if num - 1 not in num_set:

            local_len = 0
            curr = num
            while curr in num_set:
                local_len += 1
                curr += 1
            
            global_len = max(global_len, local_len)
    
    return global_len

nums = [1, 2, 3, 100, 200, 4]
print(findLongestConSeq(nums))