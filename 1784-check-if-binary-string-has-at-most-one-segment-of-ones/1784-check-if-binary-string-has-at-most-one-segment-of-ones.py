class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        i = 1
        while i < len(s) and s[i] == "1":
            i += 1
        
        if i == len(s):
            return True
        
        while i < len(s):
            if s[i] == "1":
                return False
            i += 1
        
        return True