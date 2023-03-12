class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r, res = 1, max(piles), max(piles)
        
        while l <= r:
            time = 0
            k = (l + r) // 2
            for curr in piles:
                time += math.ceil(curr / k)
            
            if time <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        
        return res