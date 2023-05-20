class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_streak_len = 0
        running_streak = 0
        nums_set = set(nums)
        
        for num in nums:
            if num - 1 not in nums_set:
                running_streak = 1
                while num + 1 in nums_set:
                    running_streak += 1
                    num += 1
                max_streak_len = max(max_streak_len, running_streak)
        
        return max_streak_len