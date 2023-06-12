class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ls, lt = len(s), len(t)
        
        if ls > lt:
            return False
        
        s_ptr, t_ptr = 0, 0
        
        while s_ptr < ls and t_ptr < lt:
            
            if s[s_ptr] == t[t_ptr]:
                s_ptr += 1
            
            t_ptr += 1
        
        return s_ptr == ls