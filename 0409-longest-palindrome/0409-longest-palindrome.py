class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for c in s:
            d[c] = 1 + d.get(c, 0)
        
        res = 0
        for k, v in d.items():
            if v >= 2:
                while d[k] > 1:
                    res += 2
                    d[k] -= 2
        
        for k, v in d.items():
            if v == 1:
                res += 1
                break
        
        return res