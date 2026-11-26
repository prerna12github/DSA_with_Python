class Solution:
    def minimumLength(self, s: str) -> int:

        n = len(s)
        i = 0
        j = n-1
        while i < j and s[i] == s[j] :
            char = s[i]
            while i < j and s[i] == char:
                i = i + 1
                while j >= i and s[j] == char:
                    j = j -1
        return j-i+1            
        