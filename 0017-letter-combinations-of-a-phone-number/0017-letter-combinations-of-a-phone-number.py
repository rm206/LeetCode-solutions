import copy
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        mapp = {'2' : "abc",
               '3' : "def",
               '4' : "ghi",
               '5' : "jkl",
               '6' : "mno",
               '7' : "pqrs",
               '8' : "tuv",
               '9' : "wxyz"}
        
        def solver(i, curr):
            # base case
            if i == len(digits):
                temp = copy.copy(curr)
                res.append("".join(temp))
                return
            
            s = mapp[digits[i]]
            for l in range(len(s)):
                curr.append(s[l]) 
                solver(i + 1, curr)
                curr.pop()
        
        res = []
        curr = []
        i = 0
        solver(i, curr)
        
        return res