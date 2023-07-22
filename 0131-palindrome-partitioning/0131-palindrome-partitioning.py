class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def is_palindrome(st):
            return st == st[::-1]
            
        def solver(i):
            if i >= len(s):
                res.append(part.copy())
                return
            
            for j in range(i, len(s)):
                if is_palindrome(s[i:j + 1]):
                    part.append(s[i:j + 1])
                    solver(j + 1)
                    part.pop()
        
        res = []
        part = []
        solver(0)
        
        return res