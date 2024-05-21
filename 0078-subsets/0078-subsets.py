class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def solver(i, curr):
            nonlocal res

            if i >= len(nums):
                res.append(curr.copy())
                return
            
            curr.append(nums[i])
            solver(i + 1, curr)

            curr.pop()
            solver(i + 1, curr)
        
        res = []
        solver(0, [])

        return res