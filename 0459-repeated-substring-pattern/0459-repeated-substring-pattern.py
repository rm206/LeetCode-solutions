import copy
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l = len(s)
        
        if l == 1:
            return False
        
        
        build = []
        for i in range(l - 1):
            if s[ : i + 1] * (l // (i + 1)) == s:
                return True
        return False