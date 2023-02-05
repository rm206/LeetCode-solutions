class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr_len = len(arr)
        if arr_len < 2:
            return [-1]
        
        rmax = arr[-1]
        for i in range(arr_len-2, -1, -1):
            temp = arr[i]
            arr[i] = rmax
            if temp > rmax:
                rmax = temp
        
        arr[-1] = -1
        return arr
    