class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = ["main"]

        for op in logs:
            if op == "../":
                if stack[-1] == "main":
                    pass
                else:
                    stack.pop()
            
            elif op == "./":
                pass
            
            else:
                stack.append(op)
        
        res = 0
        while stack[-1] != "main":
            stack.pop()
            res += 1
        
        return res