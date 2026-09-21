class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == divisor :
            return 1
        sign = 1
        if dividend >= 0 and divisor < 0 :
            sign = -1
        elif dividend <=0 and divisor > 0 :
            sign = -1
        n = abs(dividend)
        d = abs(divisor)
        q = 0
        while n >= d :
            count = 0
            while n >= (d << count + 1) :
                count = count + 1
            q = q + (1 << count) 
            n = n - (d << count)

        if sign == -1 :
            q = -q    
        if q > 2**31 - 1 :
            return 2**31 -1
        if q < -2**31:
            return -2**31     
       
        return q
                        