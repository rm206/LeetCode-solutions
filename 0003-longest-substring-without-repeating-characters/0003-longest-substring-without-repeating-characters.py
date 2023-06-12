class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        l, r, res, curr_set_len = 0, 0, 0, 0
        
        while r < len(s):
            if s[r] not in st:
                st.add(s[r])
                curr_set_len += 1
            else:
                res = max(res, curr_set_len)
                while s[r] in st:
                    st.remove(s[l])
                    curr_set_len -= 1
                    l += 1
                st.add(s[r])
                curr_set_len += 1
            
            r += 1
        
        res = max(res, curr_set_len)
        return res