class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        def solver(i):
            if i == len_nums:
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            solver(i + 1)
            subset.pop()
            
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            solver(i + 1)
        
        nums.sort()
        len_nums = len(nums)
        res = []
        subset = []
        solver(0)
        return res