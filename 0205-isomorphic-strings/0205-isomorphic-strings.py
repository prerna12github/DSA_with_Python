class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n1 = len(s)
        n2 = len(t)
        stot = {}
        ttos = {}
        if n1 != n2 :
            return False
        for i in range(n1):
            char_s = s[i]
            char_t = t[i]
            if char_s in stot :
                if stot[char_s] != char_t:
                    return False    
            else:
                stot[char_s] = char_t
            if char_t in ttos :
                if ttos[char_t] != char_s:
                    return False    
            else:
                ttos[char_t] = char_s
        return True         

        