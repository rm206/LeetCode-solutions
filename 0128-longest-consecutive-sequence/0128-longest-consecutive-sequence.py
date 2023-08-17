class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_streak = 0
        s = set(nums)
        
        for n in nums:
            if n - 1 not in s:
                val = n
                l = 0
                while val in s:
                    l += 1
                    val += 1
                max_streak = max(max_streak, l)
        
        return max_streak