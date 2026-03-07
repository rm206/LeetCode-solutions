class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def is_possible(cap):
            ctr = 1
            run_sum = 0
            for w in weights:
                if run_sum + w > cap:
                    ctr += 1
                    run_sum = w
                else:
                    run_sum += w
            return ctr <= days

        l, r = max(weights), sum(weights)
        res = sum(weights)

        while l <= r:
            mid = (l + r) // 2

            if is_possible(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res