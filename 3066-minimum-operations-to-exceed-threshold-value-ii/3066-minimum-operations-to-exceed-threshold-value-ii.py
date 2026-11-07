import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        min_heap = []
        count = 0
        for num in nums:
            heapq.heappush(min_heap,num)
        while len(min_heap) >= 2 and min_heap[0] < k:
            smallest = heapq.heappop(min_heap)
            secondSmallest = heapq.heappop(min_heap)
            form = smallest*2 + secondSmallest
            heapq.heappush(min_heap,form)
            count = count + 1
        return count    
