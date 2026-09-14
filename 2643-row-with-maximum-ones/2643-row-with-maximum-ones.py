class Solution:
 def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:

    max_ones = 0
    row_index = 0

    for i in range(len(mat)):

        count = 0

        for j in range(len(mat[i])):

            if mat[i][j] == 1:
                count += 1

        if count > max_ones:
            max_ones = count
            row_index = i

    return [row_index, max_ones]