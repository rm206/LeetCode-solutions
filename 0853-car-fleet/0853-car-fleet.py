class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        times = []
        for i in range(len(position)):
            times.append((target-position[i])/speed[i])
        
        arr = []
        for i in range(len(position)):
            arr.append((position[i], speed[i], times[i]))
        arr.sort(key= lambda x : x[0], reverse = True)
        
        for curr in arr:
            if len(stack) == 0:
                stack.append(curr[2])
            elif curr[2] > stack[-1]:
                stack.append(curr[2])
            else:
                continue
        
        return len(stack)