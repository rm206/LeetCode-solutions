class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def solver(curr, curr_set):
            if len(curr) == len(nums):
                res.append(curr.copy())
            
            for num in nums:
                if num not in curr_set:
                    curr.append(num)
                    curr_set.add(num)
                    solver(curr, curr_set)
                    curr.pop()
                    curr_set.remove(num)
        
        res = []
        curr = []
        curr_set = set()
        solver(curr, curr_set)
        
        return res