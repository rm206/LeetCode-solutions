import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, int(math.ceil(c ** 0.5))

        while l <= r:
            val = l*l + r*r
            
            if val == c:
                return True
            
            if val < c:
                l += 1
            else:
                r -= 1
        
        return False