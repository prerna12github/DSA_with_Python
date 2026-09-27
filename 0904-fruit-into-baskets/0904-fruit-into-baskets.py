class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        n = len(fruits)
        hmap ={}
        left = 0
        max_len = 0
        for right in range(n):
            hmap[fruits[right]] = hmap.get(fruits[right],0) + 1
            while len(hmap) > 2:
                hmap[fruits[left]] -= 1
                if hmap[fruits[left]] == 0:
                    del hmap[fruits[left]]
                left += 1
            max_len = max(max_len,right-left+1)
        return max_len        

        