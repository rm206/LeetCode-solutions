class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])

        def is_safe(r, c):
            return (
                r >= 0 and
                r < ROWS and
                c >= 0 and
                c < COLS and
                board[r][c] == "O" and
                (r, c) not in non_surrounded
            )

        def dfs(i, j):
            non_surrounded.add((i, j))

            for dx, dy in dirs:
                new_r, new_c = i + dx, j + dy
                if is_safe(new_r, new_c):
                    dfs(new_r, new_c)
        
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        non_surrounded = set()
        for i in range(ROWS):
            if is_safe(i, 0):
                dfs(i, 0)
            if is_safe(i, COLS-1):
                dfs(i, COLS-1)
        for j in range(COLS):
            if is_safe(0, j):
                dfs(0, j)
            if is_safe(ROWS-1, j):
                dfs(ROWS-1, j)
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O" and (i, j) not in non_surrounded:
                    board[i][j] = "X"