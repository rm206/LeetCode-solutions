class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [None] * len(nums)

        i = 0
        for n in nums:
            if n > 0:
                res[i] = n
                i += 2
        
        i = 1
        for n in nums:
            if n < 0:
                res[i] = n
                i += 2
        
        return res