from typing import List

class Solution:
    def longestPath(self,mat : List[List[int]],n : int, m : int, xs : int, ys : int, xd : int, yd : int) -> int:
        # code here
        def is_valid(x, y):
            return x >= 0 and y >= 0 and x < n and y < m and visited[x][y] == 0 and mat[x][y] == 1
        
        def solver(cx, cy, curr_len):
            if cx == xd and cy == yd:
                lengths.append(curr_len)
                return
            
            visited[cx][cy] = 1
            
            # up
            if is_valid(cx - 1, cy):
                solver(cx - 1, cy, curr_len + 1)
            # down
            if is_valid(cx + 1, cy):
                solver(cx + 1, cy, curr_len + 1)
            # left
            if is_valid(cx, cy - 1):
                solver(cx, cy - 1, curr_len + 1)
            # right
            if is_valid(cx, cy + 1):
                solver(cx, cy + 1, curr_len + 1)

            visited[cx][cy] = 0
        
        if mat[xs][ys] == 0:
            return -1
            
        visited = [[0 for j in range(m)] for k in range(n)]
        lengths = [] 
        solver(xs, ys, 0)
        
        if lengths == []:
            return -1
        else:
            return max(lengths)

#{ 
 # Driver Code Starts

class IntArray:

    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        b=IntArray().Input(4)
        
        
        mat=IntMatrix().Input(a[0], a[0])
        
        obj = Solution()
        res = obj.longestPath(mat,a[0],a[1],b[0],b[1],b[2],b[3])
        
        print(res)
        


# } Driver Code Ends