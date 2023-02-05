class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            return [nums[1], nums[0]]
        pre = [1 for _ in range(len(nums))]
        post = [1 for _ in range(len(nums))]
        i = 1
        while i < len(nums):
            pre[i] = pre[i-1] * nums[i-1]
            i += 1
        i = len(nums) - 2
        while i >= 0:
            post[i] = post[i+1] * nums[i+1]
            i -= 1
        ans = [pre[i] * post[i] for i in range(len(nums))]
        return ans

        res = [1 for _ in range(len(nums))]
        pre = 1
        for i in range(len(nums)):
            res[i] *= pre
            pre *= nums[i]
        post = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= post
            post *= nums[i]
        return res


'''
        if len(nums) == 2:
            return [nums[1], nums[0]]
        pre = [1 for _ in range(len(nums))]
        post = [1 for _ in range(len(nums))]
        i = 1
        while i < len(nums):
            pre[i] = pre[i-1] * nums[i-1]
            i += 1
        i = len(nums) - 2
        while i >= 0:
            post[i] = post[i+1] * nums[i+1]
            i -= 1
        ans = [pre[i] * post[i] for i in range(len(nums))]
        return ans

        res = [1 for _ in range(len(nums))]
        pre = 1
        for i in range(len(nums)):
            res[i] *= pre
            pre *= nums[i]
        post = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= post
            post *= nums[i]
        return res
'''
        