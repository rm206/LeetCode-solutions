class Solution:
    def reverseBits(self, n: int) -> int:
        
        res = 0
        for i in range(32):
            bit = n >> i & 1
            res += (bit << (31 - i))
        return res
            
        
'''
if n == 0:
    return 0

builder = []

for i in range(32):
    val = n % 2
    n = n >> 1
    builder.append(val)

res = 0
p = 31

for i in builder:
    res += i * pow(2, p)
    p -= 1

return res
'''