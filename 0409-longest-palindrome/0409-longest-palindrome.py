class Solution:
    def longestPalindrome(self, s: str) -> int:
        st = set()
        cnt = 0
        
        for c in s:
            if c in st:
                st.remove(c)
                cnt += 2
            else:
                st.add(c)
        
        if len(st) == 0:
            return cnt
        else:
            return cnt + 1