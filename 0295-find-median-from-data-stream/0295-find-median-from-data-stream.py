import heapq
class MedianFinder:

    def __init__(self):
        self.left_max_heap = []
        self.right_min_heap = []

    def addNum(self, num: int) -> None:

        if not self.left_max_heap or num < -self.left_max_heap[0]:
            heapq.heappush(self.left_max_heap,-num)
        else:
            heapq.heappush(self.right_min_heap,num)    

        if abs(len(self.left_max_heap) - len(self.right_min_heap)) > 1:
            val = -heapq.heappop(self.left_max_heap)   
            heapq.heappush(self.right_min_heap,val) 
        elif len(self.left_max_heap) < len(self.right_min_heap):
            val = heapq.heappop(self.right_min_heap)   
            heapq.heappush(self.left_max_heap,-val)    
        
    def findMedian(self) -> float:

        if len(self.left_max_heap) == len(self.right_min_heap) :
            return (-self.left_max_heap[0] + self.right_min_heap[0])/2

        return -self.left_max_heap[0]    

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()