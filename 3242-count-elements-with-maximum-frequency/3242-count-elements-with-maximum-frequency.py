class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = {}
        res = 0
        max_f = 0

        for n in nums:
            d[n] = 1 + d.get(n, 0)

            if d[n] > max_f:
                res = d[n]
                max_f = d[n]
            elif d[n] == max_f:
                res += d[n]
        
        return res