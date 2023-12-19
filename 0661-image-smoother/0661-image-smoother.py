import math
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        def calc(r, c):
            s = 0
            cnt = 0
            dx = [-1, 0, 1]
            dy = [-1, 0, 1]
            for x in dx:
                for y in dy:
                    ry = r + y
                    cx = c + x
                    if ry >= 0 and cx >= 0 and ry < len(img) and cx < len(img[0]):
                        s += img[ry][cx]
                        cnt += 1
            return math.floor(s/cnt)
        
        res = [[] for _ in range(len(img))]
        for row in range(len(img)):
            for col in range(len(img[0])):
                res[row].append(calc(row, col))
        
        return res