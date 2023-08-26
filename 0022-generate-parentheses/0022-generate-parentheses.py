import copy
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def helper(opening, closing, curr):
            if opening == n and closing == n:
                res.append(copy.copy(curr))
            
            if opening > n:
                return 
            
            if closing > opening:
                return
            
            curr += '('
            opening += 1
            helper(opening, closing, curr)
            
            curr = curr[:-1]
            opening -= 1
            curr += ')'
            closing += 1
            helper(opening, closing, curr)
        
        res = []
        helper(0, 0, "")
        return res