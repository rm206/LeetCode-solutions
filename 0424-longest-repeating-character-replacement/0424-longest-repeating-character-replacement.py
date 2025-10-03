class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        curr = {}
        res = 0
        maxf = 0

        while r < len(s):
            curr[s[r]] = 1 + curr.get(s[r], 0)
            maxf = max(maxf, curr[s[r]])

            while (r-l+1) - maxf > k:
                curr[s[l]] -= 1
                maxf = max(curr.values())
                l += 1
            
            res = max(res, r-l+1)

            r += 1
        
        return res