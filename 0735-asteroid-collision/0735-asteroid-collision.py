class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if a > 0:
                stack.append(a)
            
            if a < 0:
                deleted = False
                while stack and stack[-1] > 0 and not deleted:
                    prev = stack.pop()
                    if prev == abs(a):
                        deleted = True
                    elif prev >= abs(a):
                        stack.append(prev)
                        deleted = True
                if not deleted:
                    stack.append(a)
        
        return stack