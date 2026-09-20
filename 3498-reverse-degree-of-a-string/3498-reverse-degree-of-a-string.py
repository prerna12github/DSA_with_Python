class Solution:
    def reverseDegree(self, s: str) -> int:
        result = 0
        for ch in range(len(s)) :
            index = ch + 1
            value = ord('z') - ord(s[ch]) + 1
            result = result + (index * value)
        return result    
            

            

        