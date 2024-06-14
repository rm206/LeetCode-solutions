class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        arr = nums

        while l <= r:
            mid = (l + r) // 2

            if arr[mid] == target:
                return mid
            
            # left sorted
            if arr[l] <= arr[mid]:
                if arr[l] <= target and target <= arr[mid]:
                    r = mid
                else:
                    l = mid + 1
            
            # right sorted
            else:
                if arr[mid] <= target and target <= arr[r]:
                    l = mid
                else:
                    r = mid - 1
        
        return -1