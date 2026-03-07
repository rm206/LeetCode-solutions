class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0
        
        if nums[0] > nums[1]:
            return 0
        if nums[-2] < nums[-1]:
            return n-1
        
        l, r = 1, n-2

        while l <= r:
            m = (l + r) // 2

            # at the peak
            if nums[m-1] < nums[m] > nums[m+1]:
                return m
            
            # on the bottom or upward slope
            if nums[m] < nums[m + 1]:
                l = m + 1
            
            else:
                r = m - 1
