import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        if a > 0 :
            heapq.heappush(max_heap,(-a,'a'))
        if b > 0 :
            heapq.heappush(max_heap,(-b,'b'))
        if c > 0 :
            heapq.heappush(max_heap,(-c,'c'))   
        result = ''
        while max_heap:
            currCount , currChar = heapq.heappop(max_heap)
            if len(result) >=2 and result[-1] == currChar and result[-2] == currChar :
                if not max_heap:
                    break
                nextCount, nextChar = heapq.heappop(max_heap)        
                result = result + nextChar
                nextCount = nextCount + 1
                if  nextCount < 0:
                   heapq.heappush(max_heap,(nextCount,nextChar))
                heapq.heappush(max_heap,(currCount,currChar))  
            else:
                result = result +  currChar
                currCount = currCount + 1
                if currCount < 0:
                    heapq.heappush(max_heap,(currCount,currChar))
        return result                 






        