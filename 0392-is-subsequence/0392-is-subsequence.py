class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ls = len(s)
        lt = len(t)
        
        if ls > lt:
            return False
        
        p1, p2 = 0, 0
        
        while p1 < ls and p2 < lt:
            if s[p1] == t[p2]:
                p1 += 1
                p2 += 1
            else:
                p2 += 1
        
        return p1 == ls