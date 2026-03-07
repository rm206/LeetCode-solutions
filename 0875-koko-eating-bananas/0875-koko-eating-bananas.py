import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_this_will_take(rate: int) -> float:
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile/rate)
            return hrs

        l, r = 1, max(piles)
        res = max(piles)
        while l <= r:
            mid = (l + r) // 2

            hours = hours_this_will_take(mid)

            if hours <= h:
                res = mid
                r = mid - 1
            
            else:
                l = mid + 1
        
        return res