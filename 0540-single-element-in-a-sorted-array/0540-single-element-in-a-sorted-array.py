class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        n = len(nums)
        l = 0
        r = n-1
        while l < r :
            mid = l + (r-l)//2

            if (r-mid)%2 == 0:
                isEven = True
            else:
                isEven = False

            if nums[mid] == nums[mid+1]:
                if isEven:
                   l = mid+2
                else:
                    r = mid -1
            if nums[mid] != nums[mid+1]:
                if isEven:
                    r = mid
                else:
                    l = mid+1
        return nums[l]                




        