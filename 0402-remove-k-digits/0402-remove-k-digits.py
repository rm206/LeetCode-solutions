class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        num = [int(n) for n in num]
        i = 0
        
        while num and k:
            curr = num.pop(0)
            
            if not stack or stack[-1] <= curr:
                stack.append(curr)
                continue
            
            while stack and stack[-1] > curr and k:
                stack.pop()
                k -= 1
            stack.append(curr)
        
        while num:
            curr = num.pop(0)
            while stack and stack[-1] > curr and k:
                stack.pop()
                k -= 1
            stack.append(curr)
        
        while k:
            stack.pop()
            k -=1
        
        while stack and stack[0] == 0:
            stack.pop(0)
        
        if not stack:
            return "0"
        
        return "".join(map(lambda x: str(x), stack))