class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        
        temp = n
        
        mask = 0
        while temp:
            mask = (mask << 1) | 1
            temp = temp >> 1
        
        return ~n & mask