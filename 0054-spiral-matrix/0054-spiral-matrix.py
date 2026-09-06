class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        top = 0
        bottom = m-1
        left = 0
        right = n-1
        ans = []
        while top<=bottom and left<=right:

            # Left -> Right
            for i in range(left,right+1):
                ans.append(matrix[top][i])
            top = top+1
            # Top -> Bottom
            for i in range(top,bottom+1):
                ans.append(matrix[i][right])
            right = right -1
            # Right -> Left
            if top <= bottom:
              for i in range(right,left-1,-1):
                ans.append(matrix[bottom][i])
            bottom = bottom-1
            # Bottom -> Top
            if left<=right:
              for i in range(bottom,top-1,-1):
                ans.append(matrix[i][left])
            left = left+1     
        return ans                


        