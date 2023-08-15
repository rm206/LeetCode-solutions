class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_l, res_r = 0, 0
        max_len = 0
        
        for i in range(len(s)):
            
            # odd len palindrome
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > max_len:
                    res_l, res_r = l, r
                    max_len = r - l + 1
                l -= 1
                r += 1
            
            # even len palindrome
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > max_len:
                    res_l, res_r = l, r
                    max_len = r - l + 1
                l -= 1
                r += 1
        
        return s[res_l : res_r + 1]