import heapq
class Solution:
    def minStoneSum(self, piles: list[int], k: int) -> int:
        max_heap = []
        summ = 0
        for num in piles:
            heapq.heappush(max_heap,-num)
            summ = summ + num

        for i in range(k):
            largest = -heapq.heappop(max_heap)    
            remove = largest // 2
            summ = summ - remove
            largest =  largest - remove
            heapq.heappush(max_heap,-largest)

        return summ    


        