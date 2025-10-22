class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        from collections import Counter

        cnts = Counter(nums)
        target_freq = max(cnts.values())

        res = 0
        for k, v in cnts.items():
            if v == target_freq:
                res += v
        
        return res