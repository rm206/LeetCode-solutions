class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        k = goal
        mp = defaultdict(int)
        mp[0] = 1
        run_sum = 0
        res = 0
        for n in nums:
            run_sum += n

            if run_sum-k in mp:
                res += mp[run_sum-k]
            
            mp[run_sum] += 1
        
        return res