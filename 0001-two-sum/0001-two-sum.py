class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        n = len(nums)
        hmap = {}
        for i in range(n):
            need = target - nums[i]
            if need in hmap :
                return [hmap[need],i]   
            hmap[nums[i]] = i
        
        