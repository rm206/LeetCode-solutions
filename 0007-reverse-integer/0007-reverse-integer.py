class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        
        if x < 0:
            sign = -1
            x *= -1
        else:
            sign = 1
            
        while x:
            digit = x % 10
            
            if res > (2**31)/10:
                return 0
            else:
                res = (res * 10) + digit
            
            x = x // 10
        
        return sign * res