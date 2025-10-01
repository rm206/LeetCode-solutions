class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        charmap = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        for c in s:
            if c in charmap.values():
                stack.append(c)
            else:
                if stack and stack[-1] == charmap[c]:
                    stack.pop()
                else:
                    return False
        
        print(stack)
        return stack == []