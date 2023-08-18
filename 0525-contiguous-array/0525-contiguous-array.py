class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        
        c = 0
        s = {0 : -1}
        res = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                c -= 1
            else:
                c += 1
            
            if c in s:
                res = max(res, i - s[c])
            else:
                s[c] = i
        
        return res