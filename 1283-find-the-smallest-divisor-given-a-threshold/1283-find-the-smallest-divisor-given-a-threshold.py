class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def is_possible(num):
            return sum([math.ceil(x/num) for x in nums]) <= threshold

        res = math.inf
        l, r = 1, max(nums)

        while l <= r:
            mid = (l + r) // 2

            if is_possible(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res