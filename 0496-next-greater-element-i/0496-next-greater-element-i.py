class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        mapp = {}
        for i in reversed(nums2):
            while stack and stack[-1] <= i :
                stack.pop()
            if stack:
                mapp[i] = stack[-1]
            else:
                mapp[i] = -1
            stack.append(i)
        result = []
        for num in nums1:
            result.append(mapp[num])
        return result                    
        