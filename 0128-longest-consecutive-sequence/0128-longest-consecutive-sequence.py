class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        els = set(nums)

        for n in els:
            if n - 1 in els:
                pass
            else:
                ctr = 0
                i = n
                while i in els:
                    ctr += 1
                    i += 1
                res = max(res, ctr)
        
        return res