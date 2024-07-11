class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
            
        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def solver(curr, curr_len):
            if curr_len == len(digits):
                res.append(curr)
                return

            for c in keyboard[digits[curr_len]]:
                solver(curr+c, curr_len+1)
        
        res = []
        solver("", 0)
        return res