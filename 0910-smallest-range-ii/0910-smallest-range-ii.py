class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        big = nums[-1]
        small = nums[0]
        
        diff = big - small
        
        for i in range(n - 1):
            mini = min(small + k, nums[i + 1] - k)
            maxi = max(big - k, nums[i] + k)
            
            diff = min(diff, maxi - mini)
        
        return diff