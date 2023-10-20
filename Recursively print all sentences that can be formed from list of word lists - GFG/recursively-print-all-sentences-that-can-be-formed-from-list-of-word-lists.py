from typing import List


from typing import List
import copy

class Solution:
    def sentences(self, ip : List[List[str]]) -> List[List[str]]:
        # code here
        def solver(s, r):
            if r == R:
                # string = "".join(s)
                res.append(copy.copy(s))
                return
            
            for word in ip[r]:
                s.append(word)
                solver(s, r + 1)
                s.pop()
        
        res = []
        s = []
        R = len(ip)
        C = len(ip[0])
        solver(s, 0)
        return res

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



class StringMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([str(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    
    a=IntArray().Input(2)
    
    
    list=StringMatrix().Input(a[0], a[1])
    
    obj = Solution()
    res = obj.sentences(list)
    
    StringMatrix().Print(res)
    

# } Driver Code Ends