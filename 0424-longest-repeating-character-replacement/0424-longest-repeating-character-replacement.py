class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r, res, count = 0, 0, 0, {}
        
        while r < len(s):
            window_len = r - l + 1
            count[s[r]] = 1 + count.get(s[r], 0)
            
            # if window not valid, move left pointer till it is valid
            while window_len - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1      
                window_len = r - l + 1
            
            res = max(res, window_len)
            r += 1
        
        return res