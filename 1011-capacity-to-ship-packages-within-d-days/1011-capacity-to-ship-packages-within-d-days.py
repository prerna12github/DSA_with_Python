class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
        low = max(weights)
        high = sum(weights)
        while(low <= high):
            mid = (low + high)//2
            tdays = 1
            load = 0
            for i in range(n):
                if load + weights[i] > mid:
                    tdays = tdays+1
                    load = weights[i]
                else:
                    load = load + weights[i]
            if tdays <= days:
                high = mid -1
            else:
                low = mid + 1
        return low            

        