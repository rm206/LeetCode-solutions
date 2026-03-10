class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def is_safe(row, col):
            return row >= 0 and row < ROWS and col >= 0 and col < COLS and grid[row][col] == "1" and (row, col) not in visited

        def dfs(i, j):
            visited.add((i, j))
            for dx, dy in dirs:
                if is_safe(i+dx, j+dy):
                    dfs(i+dx, j+dy)
        
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        ctr = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if is_safe(i, j):
                    ctr += 1
                    dfs(i, j)
        return ctr