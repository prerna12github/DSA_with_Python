class Solution:
    def singleNumber(self, nums):

        xor = 0
        for num in nums:
            xor = xor ^ num
        diff = xor & -xor
        a = 0
        b = 0
        for num in nums:

            if num & diff:
                a = a ^ num
            else:
                b = b ^ num

        return [a, b]