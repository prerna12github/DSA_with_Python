class Solution:

    def solve(self,nums,l,r,target):
        if l > r:
            return -1
        mid = l + (r-l)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.solve(nums,mid+1,r,target)    
        else:
            return self.solve(nums,l,mid-1,target)    

    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        return self.solve(nums,0,n-1,target)
      