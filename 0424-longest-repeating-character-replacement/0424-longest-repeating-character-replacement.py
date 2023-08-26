class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        curr = {}
        res = 0
        l, r = 0, 0
        
        while r < len(s):
            
            window_len = r - l + 1
            curr[s[r]] = 1 + curr.get(s[r], 0)
            
            while window_len - max(curr.values()) > k:
                curr[s[l]] -= 1
                l += 1
                window_len = r - l + 1
            
            res = max(res, r - l + 1)
            
            r += 1
            
        return res