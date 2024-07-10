class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for op in logs:
            if op == "../":
                if depth == 0:
                    pass
                else:
                    depth -= 1
            
            elif op == "./":
                pass
            
            else:
                depth += 1
        
        return depth
        # stack = ["main"]

        # for op in logs:
        #     if op == "../":
        #         if stack[-1] == "main":
        #             pass
        #         else:
        #             stack.pop()
            
        #     elif op == "./":
        #         pass
            
        #     else:
        #         stack.append(op)
        
        # res = 0
        # while stack[-1] != "main":
        #     stack.pop()
        #     res += 1
        
        # return res