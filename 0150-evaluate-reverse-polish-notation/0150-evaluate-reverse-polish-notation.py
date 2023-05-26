class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = None
        for token in tokens:
            if token == '+' or token == '-' or token == '*' or token == '/':
                operand2 = stack.pop()
                operand1 = stack.pop()
                if token == '+':
                    stack.append(operand1 + operand2)
                if token == '-':
                    stack.append(operand1 - operand2)
                if token == '*':
                    stack.append(operand1 * operand2)
                if token == '/':
                    stack.append(int(operand1 / operand2))
            else:
                stack.append(int(token))
        
        return stack[-1]