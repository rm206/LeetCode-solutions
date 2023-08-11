class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        comp = []
        
        while x:
            val = x % 10
            comp.append(val)
            x = x // 10
        
        return comp == comp[::-1]