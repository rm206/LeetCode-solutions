class Solution:
    def largestOddNumber(self, num: str) -> str:
        start = None
        r = len(num)-1

        while r > -1:
            if int(num[r]) % 2 != 0:
                start = r
                break
            else:
                r -= 1
        
        if start is None:
            return ""
        
        return num[:r+1]