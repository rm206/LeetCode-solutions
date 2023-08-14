class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def solver(curr, visited):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for num in nums:
                if num not in visited:
                    curr.append(num)
                    visited.add(num)
                    
                    solver(curr, visited)
                    
                    curr.pop()
                    visited.remove(num)
        
        res = []
        curr = []
        visited = set()
        solver(curr, visited)
        
        return res