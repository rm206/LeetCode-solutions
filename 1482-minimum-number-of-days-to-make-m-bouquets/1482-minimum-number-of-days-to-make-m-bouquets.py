class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def is_possible(days):
            bouquets_made = 0
            ctr = 0

            for bloom in bloomDay:
                if bloom <= days:
                    ctr += 1

                    if ctr == k:
                        bouquets_made += 1
                        ctr = 0
                else:
                    ctr = 0
            
            return bouquets_made >= m

        l, r = 1, max(bloomDay)
        res = -1

        while l <= r:
            mid = (l + r) // 2

            if is_possible(mid):
                res = mid
                r = mid - 1
            
            else:
                l = mid + 1
        
        return res