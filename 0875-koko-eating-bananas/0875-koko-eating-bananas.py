import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r, res = 1, max(piles), max(piles)
        
        while l <= r:
            k = (l + r) // 2
            time = 0
            
            for curr in piles:
                time += math.ceil(curr/k)
            
            if time <= h:
                r = k - 1
                res = min(res, k)
            
            else:
                l = k + 1
        
        return res