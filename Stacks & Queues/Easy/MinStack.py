"""
Get the min value in the stack in O(1) time. 
The stack is dynamic so the min value can change.
"""

class Stack:

    def __init__(self, nums: list) -> None:
        self.stack = []
        self.minStack = []

        smallest = float("inf")
        for num in nums:
            self.stack.append(num)
            smallest = min(smallest, num)
            self.minStack.append(smallest)

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.minStack.append(val)
        else:
            top_min = self.minStack[-1]
            self.minStack.append(min(top_min, val))
        
        self.stack.append(val)
    
    def pop(self) -> None | int:
        if len(self.stack) == 0:
            return None
        
        self.minStack.pop()
        return self.stack.pop()

    def getMin(self) -> None | int:
        if len(self.minStack) == 0:
            return None
        return self.minStack[-1]

stack = Stack([1, 2, 3])
print(stack.getMin() == 1)
stack.push(-10)
print(stack.getMin() == -10)