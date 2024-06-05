class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for c in s:
            d[c] = 1 + d.get(c, 0)
        
        odd_exists = 0
        res = 0
        for k, v in d.items():
            if v >= 2:
                while d[k] > 1:
                    res += 2
                    d[k] -= 2
                if d[k] == 1:
                    odd_exists += 1
            else:
                odd_exists += 1
        
        if odd_exists:
            res += 1
        
        return res