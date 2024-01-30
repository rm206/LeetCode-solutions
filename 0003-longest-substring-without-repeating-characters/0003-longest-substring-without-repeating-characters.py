class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        curr = set()
        l, r = 0, 0
        
        while r < len(s):
            while s[r] in curr:
                curr.remove(s[l])
                l += 1
            
            curr.add(s[r])
            max_len = max(max_len, r - l + 1)
            r += 1
        
        return max_len