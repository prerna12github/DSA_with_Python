class Solution:
    def pivotIndex(self, nums: list[int]) -> int:

        n = len(nums)
        summ = 0
        for num in nums:
            summ = summ + num
        csum = 0
        for i in range(n) :
            lsum = csum
            rsum = summ - lsum - nums[i]
            if lsum == rsum:
                return i
            csum = csum + nums[i]
        return -1        
        