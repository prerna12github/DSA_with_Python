import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap,-stone)
        while len(max_heap) > 1:
            a = -heapq.heappop(max_heap)     
            b = -heapq.heappop(max_heap)  
            heapq.heappush(max_heap,-(a-b))
        result = max_heap[0]
        return -result