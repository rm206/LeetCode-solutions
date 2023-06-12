class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = len(arr)
        greatest = arr[l - 1]
        arr[l - 1] = -1
        
        if l == 1:
            return arr
        
        for i in range(l - 2, -1, -1):
            curr = arr[i]
            arr[i] = greatest
            
            if curr > greatest:
                greatest = curr
        
        return arr
            
            