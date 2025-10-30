class Solution:
    def smallestNumber(self, n: int) -> int:
        cnt = 0
        while n:
            n = n // 2
            cnt += 1
        
        res = 0
        for i in range(cnt-1, -1, -1):
            res += 2**i
        
        return res