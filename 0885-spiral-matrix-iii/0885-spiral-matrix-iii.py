class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        def is_safe(r, c):
            return r >= 0 and r < rows and c >= 0 and c < cols
        
        res = []
        res_len = 0
        ctr = 1
        rcurr, ccurr = rStart, cStart

        while res_len != rows*cols:
            for _ in range(ctr):
                if is_safe(rcurr, ccurr):
                    res.append([rcurr, ccurr])
                    res_len += 1
                ccurr += 1
            
            for _ in range(ctr):
                if is_safe(rcurr, ccurr):
                    res.append([rcurr, ccurr])
                    res_len += 1
                rcurr += 1
            
            ctr += 1

            for _ in range(ctr):
                if is_safe(rcurr, ccurr):
                    res.append([rcurr, ccurr])
                    res_len += 1
                ccurr -= 1
            
            for _ in range(ctr):
                if is_safe(rcurr, ccurr):
                    res.append([rcurr, ccurr])
                    res_len += 1
                rcurr -= 1
            
            ctr += 1

        return res