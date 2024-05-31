class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            return nums
        
        xor_all = 0
        for n in nums:
            xor_all ^= n
        
        set_bit = xor_all & -xor_all

        res = [0, 0]

        for n in nums:
            if n & set_bit:
                res[0] ^= n
            else:
                res[1] ^= n
        
        return res