class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def helper(opening: int, closing: int, curr_str: str) -> None:
            nonlocal res
            nonlocal n
            
            if opening == closing and opening == n:
                res.append(curr_str)
                return
            if opening < n:
                curr_str += '('
                helper(opening+1, closing, curr_str)
                curr_str = curr_str[:-1]
            if closing < opening:
                curr_str += ')'
                helper(opening, closing + 1, curr_str)
                curr_str = curr_str[:-1]

        
        helper(0, 0, "")
        return res