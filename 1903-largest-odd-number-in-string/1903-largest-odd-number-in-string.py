class Solution:
    def largestOddNumber(self, num: str) -> str:
        r = len(num)-1

        while r > -1:
            if int(num[r]) % 2 != 0:
                return num[:r+1]
            else:
                r -= 1
        
        return ""