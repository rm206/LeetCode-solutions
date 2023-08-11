class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr, max_len, curr_len, l = set(), 0, 0, 0
        
        for i in range(len(s)):
            while s[i] in curr:
                curr.remove(s[l])
                l += 1
                curr_len -= 1
            
            curr.add(s[i])
            curr_len += 1
            max_len = max(max_len, curr_len)
        
        return max_len