class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        i = 0
        j = n-1
        chars = list(s)
        while i < j :
            if chars[i] not in 'AaIiEeOoUu':
                i = i +1
            elif chars[j] not in 'AaIiEeOoUu':
                j = j - 1
            else:
                chars[i],chars[j] = chars[j],chars[i]
                i = i +1
                j = j - 1
        return "".join(chars)              
