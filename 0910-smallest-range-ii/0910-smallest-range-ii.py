class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        mi, ma = nums[0], nums[-1]
        ans = ma - mi
        for i in range(len(nums) - 1):
            a, b = nums[i], nums[i+1]
            ans = min(ans, max(ma-k, a+k) - min(mi+k, b-k))
        return ans
        
        
'''
        nums.sort()
        n = len(nums)
        # small = nums[0] + k
        # big = nums[n - 1] - k
        ma, mi = nums[0], nums[n - 1]
        K = k
        # diff = big - small
        diff = ma - mi
        
        for i in range(n - 1):
            # mini = min(small, nums[i + 1] - k)
            # maxi = max(big, nums[i] + k)
            
            # diff = min(diff, maxi - mini)
            a, b = nums[i], nums[i+1]
            diff = min(diff, max(ma-K, a+K) - min(mi+K, b-K))
        
        return diff
'''