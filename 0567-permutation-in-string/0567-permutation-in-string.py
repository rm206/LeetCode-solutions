class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        d1 = {}
        for c in s1:
            d1[c] = 1 + d1.get(c, 0)
        d2 = {}
        l, r = 0, 0
        for r in range(l2):
            if r - l + 1 > l1:
                if d2[s2[l]] > 1:
                     
                    d2[s2[l]] -= 1
                else:
                    d2.pop(s2[l])
                l += 1
            d2[s2[r]] = 1 + d2.get(s2[r], 0)
            if d1 == d2:
                return True
        
        return False