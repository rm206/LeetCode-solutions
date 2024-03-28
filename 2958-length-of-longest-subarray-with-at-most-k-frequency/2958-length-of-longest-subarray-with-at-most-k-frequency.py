class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:            
        curr = {}
        l, r = 0, 0
        res = 0
        
        while r < len(nums):
            curr[nums[r]] = 1 + curr.get(nums[r], 0)
            
            while not curr[nums[r]] <= k:
                curr[nums[l]] -= 1
                if curr[nums[l]] <= 0:
                    curr.pop(nums[l])
                l += 1
            
            res = max(r - l + 1, res)
            
            r += 1
        
        return res