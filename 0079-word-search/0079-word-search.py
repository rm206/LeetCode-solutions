class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def search(r, c, index):
            if index == len(word):
                return True
            
            visited.add((r, c))

            if (r-1 >= 0 and board[r-1][c] == word[index] and (r-1, c) not in visited):
                if search(r-1, c, index+1):
                    return True
            
            if (r+1 < ROWS and board[r+1][c] == word[index] and (r+1, c) not in visited):
                if search(r+1, c, index+1):
                    return True
            
            if (c-1 >= 0 and board[r][c-1] == word[index] and (r, c-1) not in visited):
                if search(r, c-1, index+1):
                    return True
            
            if (c+1 < COLS and board[r][c+1] == word[index] and (r, c+1) not in visited):
                if search(r, c+1, index+1):
                    return True
            
            visited.remove((r, c))

            return False

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0]:
                    if search(i, j, 1):
                        return True
        
        return False