class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
            
            # check if left sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target and target <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            
            # right sorted
            else:
                if nums[mid] <= target and target <= nums[r]:
                    l = mid
                else:
                    r = mid - 1
        
        return -1