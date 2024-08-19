class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = temperatures
        res = [0] * len(temperatures)
        stack = []

        for i, curr_t in enumerate(temps):
            while stack and curr_t > stack[-1][0]:
                t, index = stack.pop()
                res[index] = i - index
            stack.append([curr_t, i])
        
        return res