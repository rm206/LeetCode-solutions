class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def solver(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
            
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    solver(curr)
                    curr.pop()
        
        res = []
        curr = []
        solver(curr)
        
        return res