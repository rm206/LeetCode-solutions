class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        curr_streak, max_streak = 0, 0
        for n in s:
            if n - 1 not in s:
                curr_streak = 0
                curr = n
                while curr in s:
                    curr_streak += 1
                    curr = curr + 1
                max_streak = max(max_streak, curr_streak)
        
        return max_streak