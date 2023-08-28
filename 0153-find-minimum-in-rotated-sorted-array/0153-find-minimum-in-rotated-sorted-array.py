class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = float('inf')
        
        while l < r:
            mid = (l + r) // 2
            
            if nums[mid] >= nums[0]:
                res = min(res, nums[0])
                l = mid + 1
            else:
                r = mid
        
        return min(res, nums[l])