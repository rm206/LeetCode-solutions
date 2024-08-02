class Solution:
    def minSwaps(self, nums: List[int]) -> int:        
        count1 = nums.count(1)
        if count1 == 0:
            return 0
            
        l, r = 0, 0
        c0= 0
        res = math.inf
        n = len(nums)
        
        for r in range(2*n):
            while r-l+1 > count1:
                if nums[l%n] == 0:
                    c0 -= 1
                l += 1
            
            if nums[r%n] == 0:
                c0 += 1
            
            if r-l+1 == count1:
                res = min(res, c0)
        
        return res