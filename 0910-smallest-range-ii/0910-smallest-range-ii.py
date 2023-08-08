class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:      
        nums.sort()
        small = nums[0] 
        big = nums[-1] 
        diff = big - small
        
        for i in range(len(nums) - 1):
            mini = min(small + k, nums[i + 1] - k)
            maxi = max(big - k, nums[i] + k)
            
            diff = min(diff, maxi - mini)
        
        return diff
