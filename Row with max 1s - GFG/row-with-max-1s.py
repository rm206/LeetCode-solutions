#User function Template for python3
class Solution:

	def rowWithMax1s(self,arr, n, m):
		# code here
		
		def find_index(row):
		    res = None
		    l, r = 0, m - 1
		    
		    while l <= r:
		        mid = (l + r) // 2
		        
		        if arr[row][mid] == 1:
		            if res is None:
		                res = mid
		            else:
		                res = min(res, mid)
		            
		            r = mid - 1
		        
		        else:
		            l = mid + 1
            
            return res
		
		res = None
		res_row = -1
		for i in range(n):
		    index = find_index(i)
		    
		    if index is not None:
		        if res is None:
		            res = index
		            res_row = i
		        else:
		            if index < res:
		                res = min(res, index)
		                res_row = i
        
        return res_row


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))
        
        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                arr[i][j] = inputLine[i * m + j]
        ob = Solution()
        ans = ob.rowWithMax1s(arr, n, m)
        print(ans)
        tc -= 1

# } Driver Code Ends