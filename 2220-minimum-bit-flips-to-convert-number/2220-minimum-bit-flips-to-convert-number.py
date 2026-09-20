class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count = 0
        xor = start ^ goal
        while xor > 0 :
            rem = xor % 2
            if rem == 1:
                count = count + 1
            xor = xor // 2
        return count            
        