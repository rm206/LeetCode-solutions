class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        def is_safe(r, c):
            return r >= 0 and r < rows and c >= 0 and c < cols
        
        dirs = [[0,1],[1,0],[0,-1],[-1,0]] # right, down, left, up
        res = []
        res_len = 0
        ctr = 1
        rcurr, ccurr = rStart, cStart
        i = 0

        while res_len != rows*cols:
            for dont_matter in range(2):
                dr, dc = dirs[i]
                for _ in range(ctr):
                    if (0 <= rcurr < rows and 0 <= ccurr < cols):
                        res.append([rcurr, ccurr])
                        res_len += 1
                    rcurr, ccurr = rcurr + dr, ccurr + dc
                i = (i + 1) % 4
            
            ctr += 1

        return res

"""
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
"""