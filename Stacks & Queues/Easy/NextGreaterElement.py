"""
Find the next greater element.

[2,1,2,4,3] → [4,2,4,-1,-1]

Solution:
- Maintain a stack while traversing from the back
- if current element is greater than top element, pop
- Otherwise add to the stack
"""

# O(n)
# O(n)
def getNextGreaterElements(nums: list) -> list:
    stack = []
    result = []

    for i in range(len(nums) - 1, -1 , -1):
        # check the stack   
        while len(stack) > 0 and nums[i] >= stack[-1]:
            stack.pop()

        # add to result
        if len(stack) > 0:
            result.append(stack[-1])
        else:
            result.append(-1)

        # add to sack
        stack.append(nums[i])

    return result[::-1]

nums = [2, 1, 2, 4, 3]
result = [4, 2, 4, -1, -1]
print(getNextGreaterElements(nums) == result)