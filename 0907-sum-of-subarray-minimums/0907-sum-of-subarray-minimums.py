class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        n = len(arr)
        M = 10**9+7
        NSL = [0]*n
        NSR = [0]*n
        summ = 0
        stack = []

        #NSL
        for i in range(n):
                while stack and arr[stack[-1]] >= arr[i]:
                    stack.pop()
                NSL[i] = stack[-1] if stack else -1     
                stack.append(i) 

        stack = []              

        #NSR
        for i in range(n-1,-1,-1):
                while stack and arr[stack[-1]] > arr[i]:
                    stack.pop()
                NSR[i] = stack[-1] if stack else n  
                stack.append(i)              


        for i in range(n):
            ls = i - NSL[i]
            rs = NSR[i] - i
            totalWays = ls * rs
            totalSum = arr[i] * totalWays
            summ = (summ + totalSum) % M

        return summ    




        