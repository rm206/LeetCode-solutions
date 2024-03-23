class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        
        l, r = 0, n - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if arr[mid-1] < arr[mid] and arr[mid] > arr[mid + 1]:
                return mid
            
            elif arr[mid - 1] < arr[mid]:
                l = mid
            
            else:
                r = mid
        