class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Nov 27
        nums.sort()
        i = 0
        while i < len(nums):
            if i != nums[i]:
                return i
            i += 1
        return i
        
        return list({i for i in range(len(nums)+1)}-set(nums))[0]
        
        res = 0
        for i in range(len(nums)+1):
            res ^= i
        for i in nums:
            res ^= i
        return res
        