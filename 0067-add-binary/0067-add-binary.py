class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        res = []
        carry = 0
        while i >= 0 or j >= 0:
            v1, v2 = 0, 0
            
            if i >= 0:
                v1 = ord(a[i]) - ord('0')
            if j >= 0:
                v2 = ord(b[j]) - ord('0')
            
            val = v1 + v2 + carry
            
            res.append(str(val % 2))
            
            if val >= 2:
                carry = 1
            else:
                carry = 0
            
            i -= 1
            j -= 1
        
        if carry:
            res.append('1')
        
        res = "".join(res)
        res = res[::-1]
        return res