class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        low = 1 
        high = max(piles)
        while(low<=high):
            totalH = 0
            mid = (low+high)//2
            for i in range(n):
                totalH = totalH + ceil(piles[i]/mid)    
            if totalH <= h:
                high = mid -1
            else:
                low = mid + 1            
        return low        