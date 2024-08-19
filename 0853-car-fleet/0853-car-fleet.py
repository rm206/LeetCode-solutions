class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = [[position[i], (target-position[i])/speed[i]] for i in range(len(position))]
        arr.sort(reverse = True)

        stack = []

        for d, t in arr:
            if not stack:
                stack.append(t)
            elif t > stack[-1]:
                stack.append(t)
        
        return len(stack)