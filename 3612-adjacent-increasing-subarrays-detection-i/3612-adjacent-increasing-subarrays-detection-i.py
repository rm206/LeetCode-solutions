class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        prev_streak, curr_streak = 0, 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curr_streak += 1
            else:
                prev_streak = curr_streak
                curr_streak = 1
            
            if (curr_streak >= 2*k) or (curr_streak >= k and prev_streak >= k):
                return True
        
        return False