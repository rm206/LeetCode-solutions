class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        q = []
        res = 0
        fresh_count = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c, 0))
                if grid[r][c] == 1:
                    fresh_count += 1
        
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        while q:
            curr_r, curr_c, curr_t = q.pop(0)
            res = max(res, curr_t)

            for dr, dc in dirs:
                new_r, new_c = curr_r + dr, curr_c + dc
                if 0 <= new_r < ROWS and 0 <= new_c < COLS and grid[new_r][new_c] == 1:
                    q.append((new_r, new_c, curr_t + 1))
                    grid[new_r][new_c] = 2
                    fresh_count -= 1
        
        return res if fresh_count == 0 else -1