import copy

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def solver(curr, curr_len, openb, closedb):
            if openb == closedb and openb == n:
                res.append(copy.copy(curr))
                return
            
            if openb < n:
                solver(curr+"(", curr_len+1, openb+1, closedb)
            
            if closedb < openb:
                solver(curr+")", curr_len+1, openb, closedb+1)
        
        res = []
        solver("", 0, 0, 0)
        return res