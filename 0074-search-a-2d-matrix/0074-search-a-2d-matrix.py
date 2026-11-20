class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m * n -1 
        while(l <= r):
            mid = l + (r-l)//2
            if matrix[mid//n][mid%n] == target:     #1d to 2d mapping in array
                return True
            elif matrix[mid//n][mid%n] > target:
                r = mid -1
            else:
                l = mid + 1
        return False                