class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        res = 0
        nums.sort()

        l, r = 0, 1
        while r < len(nums):
            if nums[l] >= nums[r]:
                res += 1 + abs(nums[l] - nums[r])
                nums[r] = nums[l] + 1

            l += 1
            r += 1
        
        return res