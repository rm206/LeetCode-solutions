class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t not in "+-*/":
                stack.append(t)
            else:
                op2 = int(stack.pop())
                op1 = int(stack.pop())

                if t == "+":
                    stack.append(op1 + op2)
                
                if t == "-":
                    stack.append(op1 - op2)
                
                if t == "*":
                    stack.append(op1 * op2)
                
                if t == "/":
                    stack.append(int(op1 / op2))
        
        return int(stack[-1])