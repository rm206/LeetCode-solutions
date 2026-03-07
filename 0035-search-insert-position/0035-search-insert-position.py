class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        res = -1

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                res = mid
                l = mid + 1
            
            else:
                r = mid - 1
        
        return res+1