class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            sign = -1
            x *= -1
        else:
            sign = 1

        rev = 0
        cx = x

        while cx:
            rev = (rev * 10) + (cx % 10)
            cx = cx // 10
        
        return sign * rev == x