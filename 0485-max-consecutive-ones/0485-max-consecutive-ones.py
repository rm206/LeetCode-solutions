class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        curr = 0

        for i in nums:
            if i == 1:
                curr += 1
                res = max(res, curr)
            else:
                # res = max(res, curr)
                curr = 0
        
        return res