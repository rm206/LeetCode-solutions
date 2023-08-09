class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        comp  = [0 for i in range(26)]
        
        for c in s:
            comp[ord(c) - ord('a')] += 1
        
        for c in t:
            comp[ord(c) - ord('a')] -= 1
        
        for i in range(26):
            if comp[i] != 0:
                return False
        
        return True