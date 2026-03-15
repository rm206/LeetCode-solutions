class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def is_safe(row, col):
            return (row >= 0 and row < ROWS and 
            col >= 0 and col < COLS and 
            grid[row][col] == 1 and 
            (row, col) not in visited)

        """
        def dfs(i, j):
            visited.add((i, j))
            self.ctr += 1
            for dx, dy in dirs:
                if is_safe(i+dx, j+dy):
                    dfs(i+dx, j+dy)
        """
        def bfs(i, j):
            q = [[i, j]]
            self.ctr += 1
            visited.add((i, j))
            while q:
                r, c = q.pop(0)
                for dx, dy in dirs:
                    if is_safe(r+dx, c+dy):
                        q.append([r+dx, c+dy])
                        visited.add((r+dx, c+dy))
                        self.ctr += 1
        
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        res = 0
        self.ctr = 0
        visited = set()
        for i in range(ROWS):
            for j in range(COLS):
                if is_safe(i, j):
                    self.ctr = 0
                    # dfs(i, j)
                    bfs(i, j)
                    res = max(res, self.ctr)
        return res