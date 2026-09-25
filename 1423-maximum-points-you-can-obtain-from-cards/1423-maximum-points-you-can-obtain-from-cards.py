class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        lsum = 0
        rsum = 0
        max_sum = 0
        n = len(cardPoints)
        for i in range(0,k):
            lsum = lsum + cardPoints[i]
        max_sum = lsum
        rindex = n-1
        for i in range(k-1,-1,-1):
            lsum = lsum - cardPoints[i]
            rsum = rsum + cardPoints[rindex]
            rindex = rindex -1  
            max_sum = max(max_sum,lsum+rsum)
        return max_sum    
        