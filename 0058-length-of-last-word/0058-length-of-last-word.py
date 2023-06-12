class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ptr = len(s) - 1
        
        while s[ptr] == ' ':
            ptr -= 1
        
        res = 0
        
        while s[ptr] != ' ' and ptr > -1:
            res += 1
            ptr -= 1
        
        return res