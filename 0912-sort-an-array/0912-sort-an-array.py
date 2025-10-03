class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(arr1, arr2):
            res = []
            p1, p2 = 0, 0
            while p1 < len(arr1) or p2 < len(arr2):
                val1 = arr1[p1] if p1 < len(arr1) else math.inf
                val2 = arr2[p2] if p2 < len(arr2) else math.inf

                if val1 < val2:
                    res.append(val1)
                    p1 += 1
                else:
                    res.append(val2)
                    p2 += 1
            
            return res
        
        def mergesort(arr):
            if len(arr) == 1:
                return arr
            
            n = len(arr)
            till = n // 2
            arr1 = mergesort(arr[:till])
            arr2 = mergesort(arr[till:])
            return merge(arr1, arr2)
        
        return mergesort(nums)