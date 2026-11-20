# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        l = 1
        r = n
        while l <= n:
            guessed_number = l+(r-l)//2
            val = guess(guessed_number)
            if val == 0:
                return guessed_number
            elif val == -1:
                r = guessed_number - 1
            else:
                l = guessed_number+1
        return -1                        