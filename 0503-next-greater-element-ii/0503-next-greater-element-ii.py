
class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [-1] * n
        stack = []
        for i in range(2 * n - 1, -1, -1):
            num = nums[i % n]
            while stack and stack[-1] <= num:
                stack.pop()
            if i < n:
                if stack:
                    result[i] = stack[-1]
            stack.append(num)
        return result
