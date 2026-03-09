class Solution:
    def beautySum(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            mp = defaultdict(int)
            for j in range(i, len(s)):
                mp[s[j]] += 1
                res += max(mp.values())-min(mp.values())
        
        return res