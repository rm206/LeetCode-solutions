class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def dfs(i, run_sum, run_arr):            
            if run_sum == target:
                res.append(run_arr.copy())
                return
            
            if run_sum > target:
                return
            
            if i >= len(candidates):
                return
            
            run_arr.append(candidates[i])
            dfs(i, run_sum + candidates[i], run_arr)
            
            run_arr.pop()
            dfs(i + 1, run_sum, run_arr)
        
        i = 0
        run_sum = 0
        res = []
        run_arr = []
        dfs(i, run_sum, run_arr)
        
        return res