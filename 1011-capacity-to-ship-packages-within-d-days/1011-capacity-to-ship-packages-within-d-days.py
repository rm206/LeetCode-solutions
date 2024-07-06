class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def is_possible(target):
            ctr = 1
            curr = 0

            for w in weights:
                if curr + w <= target:
                    curr += w
                else:
                    ctr += 1
                    curr = w
            
            return ctr <= days

        l, r = max(weights), sum(weights)

        while l <= r:
            mid = (l + r) // 2

            if is_possible(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res