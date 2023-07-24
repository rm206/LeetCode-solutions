class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0
        k = 0
        
        while i + 1 < n:
            if nums[i] > nums[i + 1]:
                k += 1
            i += 1
            
        if k > 1:
            return False
        elif k == 0:
            return True
        else:
            return nums[n - 1] <= nums[0]