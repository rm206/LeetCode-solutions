class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def builder(i, curr_sum, curr_arr):
            nonlocal res

            if curr_sum > target or i >= len(candidates):
                return
            
            if curr_sum == target:
                res.append(curr_arr.copy())
                return
            
            builder(i, curr_sum+candidates[i], curr_arr+[candidates[i]])

            builder(i+1, curr_sum, curr_arr)
        
        res = []
        builder(0, 0, [])
        return res