class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        low = min(bloomDay)
        high = max(bloomDay)

        if m * k > len(bloomDay) :
            return -1
        else:    

          while low <= high:

            mid = (low + high) // 2

            bouquets = 0
            flowers = 0

            for i in range(len(bloomDay)):

                if bloomDay[i] <= mid:
                    flowers += 1

                    if flowers == k:
                        bouquets += 1
                        flowers = 0

                else:
                    flowers = 0

            if bouquets >= m:
                high = mid - 1
            else:
                low = mid + 1

        return low