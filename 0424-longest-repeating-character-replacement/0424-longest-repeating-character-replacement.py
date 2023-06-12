class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r, res, count = 0, 0, 0, {}
        
        while r < len(s):
            window_len = r - l + 1
            count[s[r]] = 1 + count.get(s[r], 0)
            
            # check if window valid, if it is update res
            if window_len - max(count.values()) <= k:
                res = max(res, window_len)
            
            # if window not valid, move left pointer till it is valid
            else:
                while window_len - max(count.values()) > k:
                    count[s[l]] -= 1
                    l += 1      
                    window_len = r - l + 1
            
            r += 1
        
        return res