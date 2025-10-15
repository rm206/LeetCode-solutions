class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        """
        2,5,7,8,9,2,3,4,3,1
        1,2,3,4,5,1,2,3,1,1      
        """

        streaks = [1]
        curr_streak = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curr_streak += 1
            else:
                curr_streak = 1
            streaks.append(curr_streak)
        
        print(streaks)
        res = 1
        for i, s in enumerate(streaks):            
            res = max(res, s//2)
            if i - s >= 0:
                res = max(res, min(s, streaks[i-s]))
        
        return res