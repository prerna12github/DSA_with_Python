class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        left_most = self.search_left(nums,target,n)
        right_most = self.search_right(nums,target,n)
        return [left_most,right_most]

    def search_left(self,nums,target,n):
        l = 0
        r = n-1
        left_most = -1
        while(l<=r):
            mid = l+ (r-l)//2
            if nums[mid] == target:
                left_most = mid
                r = mid-1
            elif nums[mid] < target:
                l = mid+1
            else:
                r = mid-1
        return left_most    

    def search_right(self,nums,target,n):
        l = 0
        r = n-1
        right_most = -1
        while(l<=r):
            mid = l+ (r-l)//2
            if nums[mid] == target:
                right_most = mid
                l = mid+1
            elif nums[mid] < target:
                l = mid+1
            else:
                r = mid-1
        return right_most                   




        