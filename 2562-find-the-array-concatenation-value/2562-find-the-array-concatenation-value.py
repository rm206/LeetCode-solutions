class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        total = 0
        l = 0
        r = len(nums) - 1
        while l < r:
            # concat = nums[l]
            # temp_pow = 10
            # while (temp_pow <= nums[r]):
            #     temp_pow *= 10
            # concat = (concat * temp_pow) + nums[r]
            # total += concat
            # l += 1
            # r -= 1
            total += eval(str(nums[l]) + str(nums[r]))
            l += 1
            r -= 1
        
        if l == r:
            total += nums[l]
        
        return total
                
        