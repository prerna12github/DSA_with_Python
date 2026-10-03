class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
       
        def atMost(k):
            if k < 0:
                return 0

            left = 0
            current_sum = 0
            count = 0
            for right in range(len(nums)):

                current_sum += nums[right] % 2

                while current_sum > k:
                    current_sum -= nums[left] % 2
                    left += 1

                count += right - left + 1

            return count

        return atMost(k) - atMost(k - 1)