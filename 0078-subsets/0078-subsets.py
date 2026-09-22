class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        subset = 2 ** n
        ans = []
        for num in range(subset):
            l = []
            for i in range(n):
                if num & (1 << i):
                    l.append(nums[i])
            ans.append(l)
        return ans            
        