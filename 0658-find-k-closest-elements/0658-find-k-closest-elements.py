class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        
        res_i = 0
        
        while l <= r:
            mid = (l + r) // 2
            
            curr_diff, res_diff = abs(arr[mid] - x), abs(arr[res_i] - x)
            
            if curr_diff < res_diff or (curr_diff == res_diff and arr[mid] < arr[res_i]):
                res_i = mid
            
            if arr[mid] > x:
                r = mid - 1
            
            elif arr[mid] < x:
                l = mid + 1
            
            else:
                break
        
        l, r = res_i, res_i
        
        for i in range(k - 1):
            if l == 0:
                r += 1
            elif r == len(arr) - 1 or abs(x - arr[l - 1]) <= abs(x - arr[r + 1]):
                l -= 1
            else:
                r += 1
        
        return arr[l : r + 1]