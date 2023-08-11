class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        run_sum = 0
        maxi = nums[0]
        
        for i in range(len(nums)):
            run_sum += nums[i]
            maxi = max(maxi, run_sum)
            
            if run_sum < 0:
                run_sum = 0
        
        return maxi