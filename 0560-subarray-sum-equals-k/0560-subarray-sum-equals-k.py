class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {}
        prefix[0] = 1
        res = 0
        running_sum = 0
        
        for i in range(len(nums)):
            running_sum += nums[i]
            diff = running_sum - k
            
            res += prefix.get(diff, 0)
            
            prefix[running_sum] = 1 + prefix.get(running_sum, 0)
        
        return res
                