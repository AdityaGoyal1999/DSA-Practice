"""
Implement a queue using stacks.

Solution:
- Dequeue
    - Empty contents of stack into another stack and it's top value is the desired value
- Enqueue
    - Simply add to the stack
"""
from StackImplementation import Stack

class Queue:
    def __init__(self, nums: list) -> None:
        self.stack = Stack(nums)

    def enqueue(self, val: int) -> None:
        self.stack.push(val)
    
    def dequeue(self) -> int:
        temp_stack = Stack([])

        while len(self.stack) > 0:
            temp_stack.push(self.stack.pop())
        
        result = temp_stack.pop()

        while len(temp_stack) > 0:
            self.stack.push(temp_stack.pop())
        
        return result
    
    def __len__(self) -> int:
        return len(self.stack)

queue = Queue([1, 2, 3, 4, 5])
print(queue.dequeue() == 1)
print(queue.enqueue(10) is None)
print(queue.dequeue() == 2)
print(len(queue) == 4)
