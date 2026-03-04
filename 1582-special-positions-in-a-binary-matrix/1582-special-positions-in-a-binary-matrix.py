class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        """
        rows
            0:1 
            1:1
            2:1
        cols
            0:2
            1:0
            2:1
        """
        r = [0 for i in range(len(mat))]
        c = [0 for i in range(len(mat[0]))]

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    r[i] += 1
                    c[j] += 1
        
        res = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and r[i] == 1 and c[j] == 1:
                    res += 1
        
        return res