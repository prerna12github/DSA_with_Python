class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        low = 1
        high = max(nums)
        while(low <= high):
            summ = 0
            mid = (low + high)//2
            for i in range(n):
                summ = summ + ceil(nums[i]/mid)
            if summ <= threshold :
                high = mid - 1
            else:
                low = mid +1
        return low                    