class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        
        while columnNumber:
            columnNumber -= 1
            val = columnNumber % 26
            res += chr(val + ord('A'))
            columnNumber = columnNumber // 26
        
        res = res[::-1]
        return res