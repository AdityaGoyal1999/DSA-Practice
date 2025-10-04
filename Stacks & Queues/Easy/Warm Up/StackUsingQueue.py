"""
Implement a stack using queues.

Solution -
    - Pop
        - Use 2 queues to emulate LIFO behaviour.
        - Evict all elements instead of the last one, that's the result
        - Put everything back in original queue
    - Push
        - Add elements as they are 
    - Peek
        - Same as pop but element not remove from data structure
"""
from QueueImplementation import Queue

class Stack:

    def __init__(self, nums: list) -> None:
        self.queue = Queue(nums)
        
    def push(self, val: int) -> None:
        self.queue.enqueue(val)

    def pop(self) -> int:
        temp_queue = Queue([])

        temp_element = None
        while len(self.queue) != 1:
            temp_element = self.queue.dequeue()
            temp_queue.enqueue(temp_element)

        result = self.queue.dequeue()

        while not len(temp_queue) == 0:
            self.queue.enqueue(temp_queue.dequeue())
        
        return result
    
    def peek(self) -> int:
        temp_queue = Queue([])

        while len(self.queue) != 1:
            temp_queue.enqueue(self.queue.dequeue())
        
        result = self.queue.dequeue()

        temp_queue.enqueue(result)

        while len(temp_queue) > 0:
            self.queue.enqueue(temp_queue.dequeue())
        
        return result

nums = [1, 2, 3, 4]
stack = Stack(nums)
stack.push(-1)
print(stack.peek() == -1)
stack.pop()
print(stack.peek() == 4)
print(stack.pop() == 4)
print(stack.peek() == 3)