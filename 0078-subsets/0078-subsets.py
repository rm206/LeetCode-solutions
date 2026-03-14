class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(index, curr):
            if index == len(nums):
                res.append(curr.copy())
                return
            
            dfs(index+1, curr)
            dfs(index+1, curr+[nums[index]])
        
        res = []
        dfs(0, [])
        return res