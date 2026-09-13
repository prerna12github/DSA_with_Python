class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        low = max(nums)
        high = sum(nums)
        while(low <= high):
            student =1
            pages = 0
            mid = (low + high)//2
            for i in range(n):
                if nums[i] + pages <= mid :
                    pages = pages + nums[i]
                else:
                    student = student + 1
                    pages = nums[i]
                    
            if k > n :
                return -1
            if student > k :
                low = mid +1
            else:
                high = mid -1
        return low        
        