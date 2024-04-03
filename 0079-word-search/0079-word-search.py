class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = set()
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        
        def is_safe(row, col, curr_index):
            return row >= 0 and row < m and col >= 0 and col < n and (row, col) not in visited and board[row][col] == word[curr_index]
        
        def find_word(row, col, curr_str, curr_index):
            curr_str += board[row][col]
            visited.add((row, col))
            
            if curr_str == word:
                return True
            
            found_one_valid_move = False
            
            for move in dirs:
                if is_safe(row+move[0], col+move[1], curr_index + 1):
                    found_one_valid_move = True
                    res = find_word(row+move[0], col+move[1], curr_str, curr_index + 1)
                    if res:
                        return res
            
            visited.remove((row, col))
            
            if not found_one_valid_move:
                return False
            return res
        
        word_found = False
        for row in range(m):
            for col in range(n):
                if board[row][col] == word[0]:
                    word_found = word_found or find_word(row, col, "", 0)
        
        return word_found