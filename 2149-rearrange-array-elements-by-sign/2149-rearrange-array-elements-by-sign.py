class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [None] * len(nums)
        pp, np = 0, 1

        for n in nums:
            if n > 0:
                res[pp] = n
                pp += 2
            else:
                res[np] = n
                np += 2
        
        return res