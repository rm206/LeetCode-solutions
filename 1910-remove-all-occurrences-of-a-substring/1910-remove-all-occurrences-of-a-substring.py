class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        i = 0
        p_len = len(part)
        s_len = len(s)

        while i < s_len:
            if i + p_len <= s_len and s[i : i + p_len] == part:
                s = s[ : i] + s[i + p_len : ]
                i = max(i - p_len, 0)
                s_len -= p_len
            else:
                i += 1
        return s