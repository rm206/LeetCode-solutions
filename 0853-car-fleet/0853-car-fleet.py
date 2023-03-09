class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p, s] for p, s in zip(position, speed)]
        pairs = sorted(pairs)[::-1]
        stack = []
        # print(pairs)
        for pos, sp in pairs:
            time = (target-pos)/sp
            if stack == []:
                stack.append(time)
            elif time <= stack[-1]:
                continue
            else:
                stack.append(time)
        
        return len(stack)
                