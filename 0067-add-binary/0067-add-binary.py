class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        res = []
        carry = 0
        while i >= 0 and j >= 0:
            v1, v2 = ord(a[i]) - ord('0'), ord(b[j]) - ord('0')
            val = v1 + v2 + carry
            
            if val == 0:
                res.append('0')
                carry = 0
            elif val == 1:
                res.append('1')
                carry = 0
            elif val == 2:
                res.append('0')
                carry = 1
            else:
                res.append('1')
                carry = 1
            
            i -= 1
            j -= 1
        
        while i >= 0:
            val = carry + (ord(a[i]) - ord('0'))
            
            if val == 0:
                res.append('0')
                carry = 0
            elif val == 1:
                res.append('1')
                carry = 0
            else:
                res.append('0')
                carry = 1
            
            i -= 1

        while j >= 0:
            val = carry + (ord(b[j]) - ord('0'))
            
            if val == 0:
                res.append('0')
                carry = 0
            elif val == 1:
                res.append('1')
                carry = 0
            else:
                res.append('0')
                carry = 1
            
            j -= 1
        
        if carry:
            res.append('1')
        
        res = "".join(res)
        res = res[::-1]
        return res