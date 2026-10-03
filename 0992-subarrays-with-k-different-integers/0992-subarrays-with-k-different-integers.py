class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        def atMost(k):
            left = 0
            count = 0
            hmap = {}
            for right in range(len(nums)):
                hmap[nums[right]] = hmap.get(nums[right],0) + 1
                while len(hmap) > k:
                    hmap[nums[left]] -= 1
                    if hmap[nums[left]] == 0:
                        del hmap[nums[left]]
                    left += 1
                count += right - left + 1
            return count
        return atMost(k) - atMost(k - 1)