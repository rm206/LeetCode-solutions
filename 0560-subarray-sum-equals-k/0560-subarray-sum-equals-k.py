class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        run_sum = 0
        prefix = {0 : 1}
        
        for n in nums:
            run_sum += n
            diff = run_sum - k
            
            res += prefix.get(diff, 0)
            
            prefix[run_sum] = 1 + prefix.get(run_sum, 0)
        
        return res