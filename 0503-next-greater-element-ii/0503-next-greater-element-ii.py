class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        stack = []

        for i in range(len(nums) * 2):
            i = i % len(nums)
            n = nums[i]

            if not stack:
                stack.append([n, i])
            else:
                while stack and n > stack[-1][0]:
                    val, index = stack.pop()
                    res[index] = n
                stack.append([n, i])
        
        return res