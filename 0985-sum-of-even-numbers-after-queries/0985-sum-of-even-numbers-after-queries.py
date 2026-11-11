class Solution:
    def sumEvenAfterQueries(self, nums: list[int], queries: list[list[int]]) -> list[int]:

        n = len(nums)
        q = len(queries)
        summ = 0
        result = []
        for i in nums:
            if i % 2 == 0:
               summ = summ + i
        for x in range(q) :
            val = queries[x][0]
            idx = queries[x][1]
            if nums[idx] % 2 == 0:
                summ = summ - nums[idx]
            nums[idx] = nums[idx] + val
            if nums[idx] % 2 == 0:
                summ = summ + nums[idx]
            result.append(summ)
        return result                   

        