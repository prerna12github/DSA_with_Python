class Solution:

    def majorityElement(self, nums: list[int]) -> list[int]:
        n = len(nums)
        count1 = 0
        count2 = 0
        cand1 = None
        cand2 = None
        for num in nums:
            if cand1 == num:
                count1 += 1

            elif cand2 == num:
                count2 += 1

            elif count1 == 0:
                cand1 = num
                count1 = 1

            elif count2 == 0:
                cand2 = num
                count2 = 1

            else:
                count1 -= 1
                count2 -= 1
        count1 = 0
        count2 = 0

        for num in nums:

            if num == cand1:
                count1 += 1

            elif num == cand2:
                count2 += 1
        result = []
        if count1 > n // 3:
            result.append(cand1)

        if count2 > n // 3:
            result.append(cand2)
        return result

