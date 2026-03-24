class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(grid), len(grid[0])
        MOD_VAL = 12345
        res = [[1 for _ in range(COLS)] for _ in range(ROWS)]

        curr = 1
        for i in range(ROWS):
            for j in range(COLS):
                res[i][j] *= curr
                curr = (curr * grid[i][j]) % MOD_VAL
        
        curr = 1
        for i in range(ROWS-1, -1, -1):
            for j in range(COLS-1, -1, -1):
                res[i][j] = (res[i][j] * curr) % MOD_VAL
                curr = (curr * grid[i][j]) % MOD_VAL
        
        return res