from collections import Counter
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0

        for i in range(len(nums) + max(nums)):
            if count[i] > 1:
                extras = count[i] - 1
                res += extras
                count[i + 1] += extras
        
        return res