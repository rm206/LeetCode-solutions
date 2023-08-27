class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        
        if x < 0:
            x *= -1
            sym = -1
        else:
            sym = 1
            
        res = 0
        
        while x:
            if res > 2**31 / 10 or res < -2**31 / 10:
                return 0
            
            res = (res * 10) + (x % 10)
            x = x // 10
        
        return sym * res