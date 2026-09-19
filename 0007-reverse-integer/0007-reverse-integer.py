class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        sign = 1
        if x < 0 :
            sign = -1
            x = -x
        while (x>0):
            digits = x % 10
            rev = rev * 10 + digits
            x = x // 10
        rev = rev * sign  
        if rev < -2 ** 31 or rev > 2 ** 31 -1:
            return 0  
        return rev    
        