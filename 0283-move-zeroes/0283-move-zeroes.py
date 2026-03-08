class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_safe = 0
        curr = 0

        for curr in range(len(nums)):
            if nums[curr] != 0:
                nums[last_safe] = nums[curr]
                last_safe += 1
        
        for i in range(last_safe, len(nums)):
            nums[i] = 0