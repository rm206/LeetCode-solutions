class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        
        for i in range(0, n + 1):
            val = 0
            while i > 0:
                val += i % 2
                i = i // 2
            res.append(val)
        
        return res