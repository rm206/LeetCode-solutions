class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def solver(i, running_sum):
            if running_sum == target:
                res.append(curr.copy())
                return
            
            if i >= len(candidates) or running_sum > target:
                return
            
            curr.append(candidates[i])
            solver(i + 1, running_sum + candidates[i])
            
            to_maybe_not_consider = curr.pop()
            
            while i + 1 < len(candidates) and candidates[i + 1] == to_maybe_not_consider:
                i += 1
            
            solver(i + 1, running_sum)
        
        candidates.sort()
        curr = []
        res = []
        solver(0, 0)
        return res