class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for i in range(len(temperatures))]
        stack = []
        
        for i in range(len(temperatures)):
            if not stack:
                stack.append((temperatures[i], i))
                continue
            
            if temperatures[i] < stack[-1][0]:
                stack.append((temperatures[i], i))
            else:
                while stack and stack[-1][0] < temperatures[i]:
                    temp, index = stack.pop()
                    res[index] = i - index
                stack.append((temperatures[i], i))
        
        return res