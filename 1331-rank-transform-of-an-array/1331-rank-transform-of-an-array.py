class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:

        hmap = {}
        rank = 1
        sorted_arr = sorted(arr)
        for num in sorted_arr :
            if num not in hmap:
                hmap[num] = rank
                rank = rank + 1
        result = []
        for i in arr :
            result.append(hmap[i])     

        return result     
        