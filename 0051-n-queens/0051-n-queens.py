class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def processed(board):
            ans = []
            
            for row in board:
                s = ""
                for place in row:
                    s += "." if place == 0 else "Q"
                ans.append(s)
            
            return ans
        
        def is_safe(row, col):
            # row
            x, y = row, col
            while y >= 0:
                if board[x][y] == 1:
                    return False
                y -= 1
            
            x, y= row, col
            while x >= 0 and y >= 0:
                if board[x][y] == 1:
                    return False
                
                x -= 1
                y -= 1
            
            x,y = row, col
            while x < n and y >= 0:
                if board[x][y] == 1:
                    return False
                
                x += 1
                y -= 1
            
            return True
        
        def solver(col):
            if col == n:
                res.append(processed(board))
                return
            
            for row in range(n):
                if is_safe(row, col):
                    board[row][col] = 1
                    solver(col + 1)
                    board[row][col] = 0
        
        
        res = []
        board = [[0 for i in range(n)] for j in range(n)]
        solver(0)
        
        return res