class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opened = 0
        res = 0

        for c in s:
            if c == "(":
                opened += 1
            else:
                if opened == 0:
                    res += 1
                opened = max(opened-1, 0)

        return opened + res