class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
       hmap ={}
       n = len(s)
       max_len = 0
       max_freq = 0
       left = 0
       for right in range(n):
          hmap[s[right]] = hmap.get(s[right] ,0 ) + 1
          max_freq = max(max_freq,hmap[s[right]])
          while(right - left + 1) - max_freq > k:
            hmap[s[left]] = hmap[s[left]] - 1
            left = left + 1
          max_len = max(max_len,right - left +1)
       return max_len     
