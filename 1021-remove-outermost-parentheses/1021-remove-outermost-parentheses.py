class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        opened = 0
        res = []

        for c in s:
            if c == "(":
                if opened > 0:
                    res.append(c)
                opened += 1
            elif c == ")":
                if opened > 1:
                    res.append(c)
                opened -= 1
        
        return "".join(res)