import copy

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        def solver(i, running_str):
            if i >= len(digits):
                res.append(copy.copy(running_str))
                return
            
            s = mapping[digits[i]]
            
            for letter in s:
                running_str += letter
                solver(i + 1, running_str)
                running_str = running_str[:-1]
                
                
                
        if digits == "":
            return []
        mapping = {"2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"}
        running_str = ""
        res = []
        solver(0, running_str)
        
        return res
            