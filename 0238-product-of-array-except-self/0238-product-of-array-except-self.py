class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [None for _ in range(len(nums))]
        
        l_mult = 1
        for i in range(len(nums)):
            res[i] = l_mult
            l_mult *= nums[i]
        
        r_mult = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * r_mult
            r_mult *= nums[i]
        
        return res
        
'''
l_mult = 1
left = []
for i in range(len(nums)):
    left.append(l_mult)
    l_mult *= nums[i]

r_mult = 1
right = [0 for _ in range(len(nums))]
for i in range(len(nums) - 1, -1, -1):
    right[i] = r_mult
    r_mult *= nums[i]

res = []
for i in range(len(nums)):
    res.append(left[i] * right[i])

return res
'''