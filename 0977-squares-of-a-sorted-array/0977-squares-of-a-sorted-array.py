class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        res = [None for i in range(len(nums))]
        place_at = len(nums) - 1
        l, r = 0, len(nums) - 1
        
        while l <= r:
            val_l, val_r = abs(nums[l]), abs(nums[r])
            
            if val_l > val_r:
                res[place_at] = pow(val_l, 2)
                l += 1
            else:
                res[place_at] = pow(val_r, 2)
                r -= 1
            
            place_at -= 1
        
        return res
        
        '''
        res = []
        mid = -1
        for i in range(len(nums)):
            if nums[i] >= 0:
                mid = i
                break
        
        if mid == -1:
            for i in range(len(nums) - 1, -1, -1):
                res.append(pow(nums[i], 2))
            return res
        
        l, r = mid - 1, mid
        
        while l >= 0 or r < len(nums):
            val_l, val_r = float('inf'), float('inf')
            if l >= 0:
                val_l = abs(nums[l])
            if r < len(nums):
                val_r = abs(nums[r])
            
            if val_l < val_r:
                res.append(pow(val_l, 2))
                l -= 1
            else:
                res.append(pow(val_r, 2))
                r += 1
        
        return res
        '''