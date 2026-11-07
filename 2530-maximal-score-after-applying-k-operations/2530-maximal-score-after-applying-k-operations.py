import heapq,math
class Solution:
    def maxKelements(self, nums: list[int], k: int) -> int:
        max_heap = []
        summ = 0
        for num in nums:
            heapq.heappush(max_heap,-num)
        while(k):
            maxEl = -heapq.heappop(max_heap)
            summ = summ + maxEl
            maxEl = math.ceil(maxEl/3.0)
            heapq.heappush(max_heap,-maxEl)
            k = k -1 
        return summ        

        