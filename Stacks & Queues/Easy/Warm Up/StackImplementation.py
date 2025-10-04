"""
Implement a stack and support push, pop and peek
"""

class Stack:

    def __init__(self, nums: list) -> None:
        self.stack = []

        for num in nums:
            self.stack.append(num)
    
    def push(self, val: int) -> None:
        self.stack.append(val)
    
    def pop(self) -> int | None:

        if len(self.stack) == 0:
            return None
        
        top_val = self.stack.pop()
        return top_val
    
    def peek(self) -> int | None:

        if len(self.stack) == 0:
            return None
        
        return self.stack[-1]


nums = [1, 2, 3, 4]
stack = Stack(nums)
stack.push(-1)
print(stack.peek() == -1)
stack.pop()
print(stack.peek() == 4)
print(stack.pop() == 4)
print(stack.peek() == 3)