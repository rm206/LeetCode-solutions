class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1

        while l <= r:
            mid = (l + r) // 2

            if mid > 0 and arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
                return mid
            
            if arr[mid - 1] < arr[mid]:
                l = mid

            else:
                r = mid
        
         