class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        n = len(num)
        stack = []
        for i in range(n):
            while stack and stack[-1] > num[i] and k > 0 :
                stack.pop()
                k = k -1
            stack.append(num[i])    
        while k > 0 :
            stack.pop()      
            k = k-1 

        result = "".join(stack)
        result = result.lstrip('0')    #remove leading zeroes

        if not result:
            return '0'

        return result    

     

        