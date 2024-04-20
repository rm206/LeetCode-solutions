class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def add(row, col):
            nonlocal m, n
            
            start_x, start_y = row, col
            end_x, end_y = row, col
            
            while end_x+1 < m and land[end_x + 1][end_y] == 1:
                end_x += 1
            while end_y+1 < n and land[end_x][end_y + 1] == 1:
                end_y += 1
            
            for i in range(start_x, end_x + 1):
                for j in range(start_y, end_y + 1):
                    land[i][j] = 0
            
            return [start_x, start_y, end_x, end_y]
            
        m, n = len(land), len(land[0])
        res = []
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    res.append(add(i, j))
        
        return res