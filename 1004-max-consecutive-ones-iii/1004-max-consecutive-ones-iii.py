class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r, count = 0, 0, {0 : 0, 1 : 0}
        res = 0
        
        while r < len(nums):
            window_len = r - l + 1
            count[nums[r]] += 1
            while l <= r and window_len - count[1] > k:
                count[nums[l]] -= 1
                l += 1
                window_len = r - l + 1
            
            window_len = r - l + 1
            
            res = max(res, window_len)
            r += 1
        
        return res