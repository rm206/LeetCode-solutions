class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for c in s:
            if c == '(' or c.isalpha():
                stack.append(c)
            else:
                temp = []
                ch = stack.pop()
                while ch != "(":
                    temp.append(ch)
                    ch = stack.pop()
                for ch in temp:
                    stack.append(ch)

        return "".join(stack)