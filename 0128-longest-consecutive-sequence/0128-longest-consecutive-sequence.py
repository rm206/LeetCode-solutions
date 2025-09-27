class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        
        s = set(nums)

        res = 0

        for n in s:
            if n-1 not in s:
                curr_streak = 1
                curr_val = n
                while curr_val+1 in s:
                    curr_streak += 1
                    curr_val += 1
                res = max(res, curr_streak)
        
        return res