class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        mp = {}
        left = 0
        max_len = 0
        for right in range(n):
            if s[right] in mp:
                left = max(left,mp[s[right]] + 1)
            mp[s[right]] = right
            max_len = max(max_len , right - left +1)
        return max_len        

             
        