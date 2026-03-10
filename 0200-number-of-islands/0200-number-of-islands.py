class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or grid[i][j] != "1":
                return
            visited.add((i, j))
            if (i+1, j) not in visited:
                dfs(i+1, j)
            if (i-1, j) not in visited:
                dfs(i-1, j)
            if (i, j+1) not in visited:
                dfs(i, j+1)
            if (i, j-1) not in visited:
                dfs(i, j-1)
        
        ctr = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == "1":
                    ctr += 1
                    dfs(i, j)
        return ctr