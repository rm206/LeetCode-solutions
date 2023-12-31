class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        p = len(s) - 1
        
        while not s[p].isalnum():
            p -= 1
        
        res = ""
        
        while p>= 0 and s[p].isalnum():
            res = res + s[p]
            p -= 1
        
        return len(res)