class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:

        m = len(mat)
        n = len(mat[0])

        low = 0
        high = n - 1

        while low <= high:

            mid = (low + high) // 2

            # Find maximum element in middle column
            max_row = 0

            for i in range(m):
                if mat[i][mid] > mat[max_row][mid]:
                    max_row = i

            # Current element
            current = mat[max_row][mid]

            # Left and right values
            left = mat[max_row][mid - 1] if mid > 0 else -1
            right = mat[max_row][mid + 1] if mid < n - 1 else -1

            # Check if current is a peak
            if current > left and current > right:
                return [max_row, mid]

            # Move towards the bigger neighbor
            elif right > current:
                low = mid + 1

            else:
                high = mid - 1