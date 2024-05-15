class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def is_safe(row, col):
            nonlocal m, n
            return row >= 0 and row < m and col >= 0 and col < n and grid[row][col] != 0 and visited[row][col] == 0

        def find(row, col, run_sum):
            nonlocal res, moves

            visited[row][col] = 1
            run_sum += grid[row][col]
            at_least_one_move = False
            for move in moves:
                if is_safe(row+move[0], col+move[1]):
                    at_least_one_move = True
                    find(row+move[0], col+move[1], run_sum)
            
            visited[row][col] = 0
            if not at_least_one_move:
                res = max(res, run_sum)

        visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        res = 0
        m, n = len(grid), len(grid[0])
        moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for row in range(m):
            for col in range(n):
                if grid[row][col] != 0:
                    find(row, col, 0)
        
        return res