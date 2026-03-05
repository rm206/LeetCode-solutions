class Solution:
    def minOperations(self, s: str) -> int:
        start0, start1 = 0, 0

        for i, c in enumerate(s):
            if i%2 == 0:
                start0 += (1 if c == '0' else 0)
                start1 += (1 if c == '1' else 0)
            else:
                start0 += (1 if c == '1' else 0)
                start1 += (1 if c == '0' else 0)
        
        return min(start0, start1)