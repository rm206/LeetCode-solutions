class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
#         if x < 0:
#             return False
#         if x < 10:
#             return True
        
#         res = 0
#         temp = x
#         while temp != 0:
#             res = (res * 10) + (temp % 10)
#             temp = temp // 10
        
#         return res == x