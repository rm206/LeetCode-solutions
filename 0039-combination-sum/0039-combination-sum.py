class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def solver(i, cur, running_sum):
            if running_sum == target:
                res.append(cur.copy())
                return
            
            if i >= len(candidates) or running_sum > target:
                return
            
            cur.append(candidates[i])
            solver(i, cur, running_sum + candidates[i])
            
            cur.pop()
            solver(i + 1, cur, running_sum)
        
        
        res = []
        solver(0, [], 0)
        return res