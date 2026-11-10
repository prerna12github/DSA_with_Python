
class Solution:
    def findOriginalArray(self, changed: list[int]) -> list[int]:

        n = len(changed)
        if n %2 != 0:
            return []
        hmap = {}
        changed.sort()
        for num in changed:
            hmap[num] = hmap.get(num,0) + 1
        original = []
        for num in changed:
            if hmap.get(num,0) == 0:
                continue
            if hmap.get(2 * num,0) == 0:
                return []
            original.append(num)
            hmap[num] -= 1
            hmap[2 * num] -= 1
        return original
