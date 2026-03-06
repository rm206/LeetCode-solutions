class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        run_sum = 0

        for n in nums:
            if n == 1:
                run_sum += 1
                res = max(res, run_sum)
            else:
                run_sum = 0
        
        return res