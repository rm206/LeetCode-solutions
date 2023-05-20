class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        pre = [1 for i in range(len_nums)]
        post = [1 for i in range(len_nums)]
        
        running_mult = 1
        for i in range(0, len_nums):
            pre[i] = running_mult
            running_mult *= nums[i]
        
        running_mult = 1
        for i in range(len_nums - 1, -1, -1):
            post[i] = running_mult
            running_mult *= nums[i]

        res = []
        for i in range(len_nums):
            res.append(pre[i] * post[i])
        
        return res