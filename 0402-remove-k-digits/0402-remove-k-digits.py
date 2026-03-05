class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for c in num:
            while stack and stack[-1] > c and k > 0:
                stack.pop()
                k -= 1
            
            stack.append(c)

        while stack and k > 0:
            stack.pop()
            k -= 1
        
        if not stack:
            return "0"
        
        i = 0
        while i < len(stack) and stack[i] == "0":
            i += 1
        
        if i == len(stack):
            return "0"
        else:
            return "".join(stack[i:])