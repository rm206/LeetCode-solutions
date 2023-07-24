class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        temp = nums.copy()
        
        for i in range(len(nums)):
            temp[(i + k) % len(nums)] = nums[i]
        
        for i in range(len(temp)):
            nums[i] = temp[i]
        