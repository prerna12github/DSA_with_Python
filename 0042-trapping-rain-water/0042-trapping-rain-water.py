class Solution:
        def getLeftMaxArray(self,height,n):
            leftMax = [0]*n
            leftMax[0] = height[0]
            for i in range(1,n):
                leftMax[i] = max(leftMax[i-1],height[i])
            return leftMax

        def getRightMaxArray(self,height,n):
            rightMax = [0]*n
            rightMax[n-1] = height[n-1]
            for i in range(n-2,-1,-1):
                rightMax[i] = max(rightMax[i+1],height[i])
            return rightMax

        def trap(self, height: list[int]) -> int:
            n = len(height)
            leftMax = self.getLeftMaxArray(height, n)
            rightMax = self.getRightMaxArray(height, n)
            summ = 0
            for i in range(n):
                h = min(leftMax[i], rightMax[i]) - height[i]
                summ += h

            return summ 


       

                        

        