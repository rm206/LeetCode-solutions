import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        
        return round(math.log(n ,2), 10) == int(math.log(n ,2))