from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        mp[0] = 1
        run_sum = 0
        res = 0
        for n in nums:
            run_sum += n
            
            res += mp.get(run_sum-k, 0)
            
            mp[run_sum] += 1
        
        return res