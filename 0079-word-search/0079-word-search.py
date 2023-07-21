class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def is_safe(row, col):
            return row >= 0 and row < m and col >= 0 and col < n and visited[row][col] == 0
        
        def solver(index, i, j):
            if index == word_len - 1:
                return True
            
            visited[i][j] = 1
            
            if is_safe(i - 1, j) and board[i - 1][j] == word[index + 1]:
                word_in_up = solver(index + 1, i - 1, j)
                if word_in_up:
                    return True
            
            if is_safe(i + 1, j) and board[i + 1][j] == word[index + 1]:
                word_in_down = solver(index + 1, i + 1, j)
                if word_in_down:
                    return True
            
            if is_safe(i, j - 1) and board[i][j - 1] == word[index + 1]:
                word_in_left = solver(index + 1, i, j - 1)
                if word_in_left:
                    return True
            
            if is_safe(i, j + 1) and board[i][j + 1] == word[index + 1]:
                word_in_right = solver(index + 1, i, j + 1)
                if word_in_right:
                    return True
            
            visited[i][j] = 0
            
            return False
        
        word_len = len(word)
        m, n = len(board), len(board[0])
        visited = [[0 for row in range(n)] for j in range(m)]
        for row in range(m):
            for col in range(n):
                if board[row][col] == word[0]:
                    found_with_curr_start_index = solver(0, row, col)
                    if found_with_curr_start_index:
                        return True
        return False