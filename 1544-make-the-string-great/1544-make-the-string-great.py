class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if stack == []:
                stack.append(c)
            elif (stack[-1].lower() == c.lower()) and ((stack[-1].islower() and c.isupper()) or (stack[-1].isupper() and c.islower())):
                stack.pop()
            else:
                stack.append(c)
        
        s = "".join(stack)
        return s