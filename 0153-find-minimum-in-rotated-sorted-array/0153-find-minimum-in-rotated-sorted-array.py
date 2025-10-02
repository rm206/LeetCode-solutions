class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = math.inf
        
        while l <= r:
            mid = (l+r) // 2

            if nums[l] <= nums[mid] >= nums[r]:
                res = min(res, nums[l])
                l = mid + 1
            elif nums[l] <= nums[mid] <= nums[r]:
                res = min(res, nums[l])
                r = mid - 1
            else: # nums[mid] <= nums[r]
                res = min(res, nums[mid])
                r = mid - 1
        
        return res
