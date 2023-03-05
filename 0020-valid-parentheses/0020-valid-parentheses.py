class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = [s[0]]

        for i in s[1:]:
            if i in "({[":
                stack.append(i)
            else:
                if i == ')':
                    if len(stack) != 0 and stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                if i == '}':
                    if len(stack) != 0 and stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                if i == ']':
                    if len(stack) != 0 and stack[-1] == '[':
                        stack.pop()
                    else:
                        return False

        return len(stack) == 0