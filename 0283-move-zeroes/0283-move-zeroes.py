class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        fix = -1
        for i in range(0, len(nums)):
            if nums[i] == 0:
                fix = i
                break
        
        if fix == -1 or fix == len(nums):
            return
        
        for i in range(fix+1, len(nums)):
            if nums[i] != 0:
                nums[i], nums[fix] = nums[fix], nums[i]
                fix += 1
        