class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ''
        count = 0
        for ch in s :
            if ch == '(':
                count = count + 1
                if count > 1 :
                    result =  result + ch
            else:
                count = count - 1
                if count > 0 :
                    result = result + ch
        return result                                
