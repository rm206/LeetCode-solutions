class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if not stack:
                stack.append(a)
            else:
                if a > 0:
                    stack.append(a)
                else:
                    val = a
                    while stack and val < 0 and stack[-1] > 0:
                        top = stack.pop()

                        if top > abs(val):
                            val = top
                        elif abs(val) > top:
                            val = val
                        else:
                            val = 0
                        
                    if val != 0:
                        stack.append(val)
        
        return stack