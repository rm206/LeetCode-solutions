class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        for curr in tokens:
            if curr == "+":
                o2 = res.pop()
                o1 = res.pop()
                res.append(o1 + o2)
            elif curr == "-":
                o2 = res.pop()
                o1 = res.pop()
                res.append(o1 - o2)
            elif curr == "*":
                o2 = res.pop()
                o1 = res.pop()
                res.append(o1 * o2)
            elif curr == "/":
                o2 = res.pop()
                o1 = res.pop()
                res.append(trunc(o1/o2))
            else:
                res.append(int(curr))
        
        return res[-1]
            