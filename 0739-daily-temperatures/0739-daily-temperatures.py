class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for i in range(len(temperatures))]
        
        for i, v in enumerate(temperatures):
            if len(stack) == 0:
                stack.append((i, v))
            else:
                if v <= stack[-1][1]:
                    stack.append((i, v))
                else:
                    while len(stack) != 0 and stack[-1][1] < v:
                        popped_index, popped_temp = stack.pop()
                        res[popped_index] = i - popped_index
                    stack.append((i, v))
        
        return res