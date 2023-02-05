class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        len_s = len(s)
        p = len_s - 1
        
        while s[p] == " " and p >= 0:
            p -= 1
        
        res = 0
        while s[p] != " " and p >= 0:
            res += 1
            p -= 1
        
        return res