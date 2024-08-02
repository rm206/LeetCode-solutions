class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        arr = nums
        
        count1 = nums.count(1)
        if count1 == 0:
            return 0
            
        l, r = 0, 0
        c0, c1 = 0, 0
        res = math.inf
        n = len(arr)
        
        for r in range(2*n):
            while r-l+1 > count1:
                if arr[l%n] == 0:
                    c0 -= 1
                else:
                    c1 -= 1
                l += 1
            
            if arr[r%n] == 0:
                c0 += 1
            else:
                c1 += 1
            
            if r-l+1 == count1:
                res = min(res, c0)
        
        return res