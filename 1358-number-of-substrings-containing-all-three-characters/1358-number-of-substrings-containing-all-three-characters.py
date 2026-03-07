class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        seen = {
            "a" : -1,
            "b" : -1,
            "c" : -1
        }

        res = 0

        for r in range(len(s)):
            seen[s[r]] = r
            if seen["a"] != -1 and seen["b"] != -1 and seen["c"] != -1:
                res += min(seen.values())+1
        
        return res