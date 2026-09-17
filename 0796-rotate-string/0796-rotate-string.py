class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n1 = len(s)
        n2 = len(goal)
        if n1 != n2:
            return False
        doublee = s + s
        if goal in doublee :
                return True
        else :
                return False        
        