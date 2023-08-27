class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def transpose(n):
            for i in range(n):
                for j in range(n):
                    if i <= j:
                        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        n = len(matrix)
        
        transpose(n)
        
        for i in range(n):
            matrix[i].reverse()