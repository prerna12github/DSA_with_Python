class Solution:
    def countCommas(self, n: int) -> int:

        result = 0
        x = 1000

        while x <= n:
            result += n - x + 1
            x *= 1000

        return result