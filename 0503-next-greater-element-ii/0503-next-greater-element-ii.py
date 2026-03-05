class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)

        res = [-1] * n
        stack = []
        for i in range(2*n):
            curr_index = i % n
            curr_val = nums[curr_index]

            while stack and stack[-1][0] < curr_val:
                _, index = stack.pop()
                res[index%n] = curr_val
            
            stack.append([curr_val, i])
        
        return res