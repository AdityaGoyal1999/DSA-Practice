"""
Get the kth largest element in the array.

Solution: 
    - Use heap to get answer. Min heap on k large elements

TODO: Complete quickselect part as well
"""
import heapq

# O(n log k)
# O(k)
def getKthLargest(nums: list, k: int) -> int:

    heap = []
    heapq.heapify(heap)

    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        else:
            if heap[0] < num:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
    
    return heap[0]


nums = [1, 2, 3, 4, 5, 6]
print(getKthLargest(nums, 3))