class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rev(start, finish):
            l, r = start, finish
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        k = k % len(nums)
        rev(0, len(nums)-k-1)
        rev(len(nums)-k, len(nums)-1)
        rev(0, len(nums)-1)