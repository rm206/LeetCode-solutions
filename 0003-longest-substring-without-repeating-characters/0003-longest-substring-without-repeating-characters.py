class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        set_curr = set({})
        for r in range(len(s)):
            while s[r] in set_curr:
                set_curr.remove(s[l])
                l += 1
            set_curr.add(s[r])
            res = max(res, r - l + 1)
        return res