class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                i_temp, t_temp = stack.pop()
                res[i_temp] = i - i_temp
            stack.append((i, t))
        
        return res
                