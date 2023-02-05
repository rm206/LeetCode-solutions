class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        curr_streak_len = 0
        max_streak_len = 0
        for curr in nums:
            if curr - 1 in s:
                continue
            else:
                curr_streak_len = 0
                temp = curr
                while temp + 1 in s:
                    curr_streak_len += 1
                    temp += 1
                curr_streak_len += 1
                if curr_streak_len > max_streak_len:
                    max_streak_len = curr_streak_len
        
        return max_streak_len

'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Dec 3
        s = set(nums)
        curr_streak_len = 0
        max_streak_len = 0
        
        for curr in s:
            if curr-1 in s:
                continue
            else:
                temp = curr
                curr_streak_len = 0
                while temp+1 in s:
                    curr_streak_len += 1
                    temp += 1
                curr_streak_len += 1
                if curr_streak_len > max_streak_len:
                    max_streak_len = curr_streak_len
                
        return max_streak_len
'''