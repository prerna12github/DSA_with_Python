class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        max_count = 0
        for ch in s :
            if ch == '(' :
                count = count + 1
                max_count = max(max_count , count)
            elif ch == ')':
                count = count - 1
            else :
                continue    
        return max_count            
        