class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        gtor = arr[n - 1]
        for i in range(n - 2, -1, -1):
            temp = arr[i]
            arr[i] = gtor
            gtor = max(gtor, temp)
        
        arr[n - 1] = -1
        
        return arr