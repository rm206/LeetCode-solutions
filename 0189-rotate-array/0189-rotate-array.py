class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        
        l, r = 0, n - k - 1
        nums[l : r + 1] = nums[l : r + 1][::-1]
        
        l, r = n - k, n - 1
        nums[l : r + 1] = nums[l : r + 1][::-1]
        
        nums.reverse()