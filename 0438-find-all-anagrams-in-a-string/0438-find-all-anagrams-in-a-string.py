class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        angp = [0 for i in range(26)]
        angs = [0 for i in range(26)]
        res = []
        
        for i in range(len(p)):
            angp[ord(p[i]) - ord('a')] += 1
        
        l, r = 0, len(p) - 1
        for i in range(l, r + 1):
            angs[ord(s[i]) - ord('a')] += 1
        
        while r < len(s):
            if r - l + 1 > len(p):
                angs[ord(s[l]) - ord('a')] -= 1
                l += 1
            
            if angs == angp:
                res.append(l)
            
            r += 1
            if r < len(s):
                angs[ord(s[r]) - ord('a')] += 1
        
        return res