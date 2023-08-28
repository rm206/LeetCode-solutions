class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = float('inf')
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            res = min(res, nums[mid])
            if nums[l] <= nums[mid]:
                res = min(res, nums[l])
                l = mid + 1
            
            elif nums[mid] <= nums[r]:
                res = min(res, nums[r])
                r = mid - 1
        
        return res