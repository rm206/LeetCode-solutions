class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        curr = 1
        for i, n in enumerate(nums):
            res[i] *= curr
            curr *= n
        
        curr = 1
        for i in range(len(nums)-1, -1, -1):
            n = nums[i]
            res[i] *= curr
            curr *= n
        
        return res