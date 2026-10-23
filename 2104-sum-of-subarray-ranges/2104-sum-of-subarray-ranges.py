class Solution:
    def subArrayRanges(self, nums: list[int]) -> int:
        n = len(nums)
        M = 10**9+7
        NSL = [0]*n
        NSR = [0]*n
        sumMin = 0
        stack = []

        # sum of subarray minimums
        #NSL
        for i in range(n):
                while stack and nums[stack[-1]] >= nums[i]:
                    stack.pop()
                NSL[i] = stack[-1] if stack else -1     
                stack.append(i) 

        stack = []              

        #NSR
        for i in range(n-1,-1,-1):
                while stack and nums[stack[-1]] > nums[i]:
                    stack.pop()
                NSR[i] = stack[-1] if stack else n  
                stack.append(i)              


        for i in range(n):
            ls = i - NSL[i]
            rs = NSR[i] - i
            totalWays = ls * rs
            sumMin += nums[i] * totalWays


        # sum of subarray maximums

        NGL = [0]*n
        NGR = [0]*n
        sumMax = 0
        stack = []

        #NGL
        for i in range(n):
                while stack and nums[stack[-1]] <= nums[i]:
                    stack.pop()
                NGL[i] = stack[-1] if stack else -1     
                stack.append(i) 

        stack = []              

        #NGR
        for i in range(n-1,-1,-1):
                while stack and nums[stack[-1]] < nums[i]:
                    stack.pop()
                NGR[i] = stack[-1] if stack else n  
                stack.append(i)              


        for i in range(n):
            ls = i - NGL[i]
            rs = NGR[i] - i
            totalWays = ls * rs
            sumMax += nums[i] * totalWays
        
        return sumMax - sumMin






        