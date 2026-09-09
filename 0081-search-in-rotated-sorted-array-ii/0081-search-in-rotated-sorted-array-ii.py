class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        low = 0
        high = n-1
        while(low<=high):
            mid = (low+high)//2
            if target == nums[mid]:
                return True
            if nums[low] == nums[mid] and nums[mid] == nums[high]:
                low = low+1
                high = high-1
                continue
        
            if nums[low] <= nums[mid]:
                    if target >= nums[low] and target <= nums[mid]:
                        high = mid-1
                    else:
                        low = mid+1
            else:
                    if target >= nums[mid] and target <= nums[high]:
                        low = mid+1
                    else:
                        high = mid -1            
        return False
        