class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n-1
        minn = float('inf')
        while(low <= high):
            mid = (low+high)//2
            if nums[low]<=nums[mid]:
                minn = min(minn,nums[low])
                low = mid+1
            else:
                high = mid-1
                minn = min(minn,nums[mid])
               
        return minn            


        