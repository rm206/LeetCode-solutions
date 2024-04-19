class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def is_safe(row, col):
            return row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0]) and grid[row][col] == "1" and visited[row][col] == False
        
        def recurse(row, col):
            nonlocal visited, dirs
            visited[row][col] = True
            
            for dx, dy in dirs:
                if is_safe(row+dx, col+dy):
                    recurse(row+dx, col+dy)
        
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and visited[i][j] == False:
                    res += 1
                    recurse(i, j)
        return res