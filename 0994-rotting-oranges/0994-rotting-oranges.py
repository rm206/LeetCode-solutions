class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def is_safe(i, j):
            return (
                i >= 0 and
                i < ROWS and
                j >= 0 and
                j < COLS and
                grid[i][j] == 1
            )

        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = []
        fresh_o = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append([i, j, 0])
                if grid[i][j] == 1:
                    fresh_o += 1
        
        max_time = 0

        while q:
            r, c, time = q.pop(0)
            max_time = max(max_time, time)

            for dx, dy in dirs:
                new_r, new_c = r+dx, c+dy
                if is_safe(new_r, new_c):
                    grid[new_r][new_c] = 2
                    fresh_o -= 1
                    q.append([new_r, new_c, time+1])
        
        return max_time if fresh_o == 0 else -1