class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if j > i:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]