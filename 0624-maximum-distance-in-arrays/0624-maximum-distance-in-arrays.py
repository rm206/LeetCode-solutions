import math

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mini, maxi = math.inf, -math.inf
        res = -math.inf

        for a in arrays:
            mn, mx = a[0], a[-1]

            res = max(res, maxi-mn, mx - mini)

            mini = min(mini, mn)
            maxi = max(maxi, mx)
        
        return res