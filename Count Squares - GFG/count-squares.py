#User function Template for python3
import math

class Solution:
    def countSquares(self, N):
        # code here 
        # count = 0
        
        # i = 1
        # while i * i < N:
        #     count += 1
        #     i += 1
        
        # return count
        return int(math.sqrt(N - 1))
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import math

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.countSquares(N))
# } Driver Code Ends