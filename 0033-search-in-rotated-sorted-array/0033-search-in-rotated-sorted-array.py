class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def get_pivot(arr, n):
	        l, r = 0, n - 1

	        while l < r:
		        mid = (l + r) // 2

		        if arr[mid] >= arr[0]:
			        l = mid + 1
		        else:
			        r = mid
	
	        return l

        def bin_search(arr, l, r, target):
	        while l <= r:
		        mid = (l + r) // 2

		        if arr[mid] == target:
			        return mid
		
		        elif arr[mid] < target:
			        l = mid + 1
		
		        else:
			        r = mid - 1
	
	        return -1

        n = len(nums)
        k = target
        pivot = get_pivot(nums, n)

        if nums[pivot] <= k and k <= nums[n - 1]:
            return bin_search(nums, pivot, n - 1, k)

        else:
            return bin_search(nums, 0, pivot - 1, k)

'''
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
            
            # left sorted portion
            if nums[l] <= nums[mid]:
                # target < nums[l] -> go right
                # target > nums[mid] -> go right
                # else go left
                if target < nums[l] or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            
            # right sorted portion
            else:
                # target > nums[r] -> go left
                # target < nums[mid] -> go left
                # else go right
                if target > nums[r] or target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return -1
'''