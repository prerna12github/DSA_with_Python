class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mapp = {0: 1}
        result = 0
        summ = 0

        for num in nums:
            summ += num

            if summ - k in mapp:
                result += mapp[summ - k]

            mapp[summ] = mapp.get(summ, 0) + 1

        return result

