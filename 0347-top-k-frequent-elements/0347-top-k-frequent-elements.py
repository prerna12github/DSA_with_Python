import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num,0) + 1

        heap = [] 
        for num,count in hashmap.items():
            heapq.heappush(heap,(count,num))
            if len(heap) > k :
                heapq.heappop(heap)

        result = []
        for count,num in heap:
            result.append(num)
        return result               