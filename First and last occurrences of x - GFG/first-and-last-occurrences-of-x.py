#User function Template for python3


class Solution:
    def find(self, arr, n, x):
        
        # code here
        l, r = 0, n - 1
        left_most = float('inf')
        
        while l <= r:
            mid = (l + r) // 2
            
            if arr[mid] == x:
                left_most = min(left_most, mid)
                r = mid - 1
            
            elif arr[mid] > x:
                r = mid - 1
            
            else:
                l = mid + 1
        
        if left_most >= n:
            return [-1, -1]
        
        l, r = 0, n - 1
        right_most = float('-inf')
        
        while l <= r:
            mid = (l + r) // 2
            
            if arr[mid] == x:
                right_most = max(right_most, mid)
                l = mid + 1
            
            elif arr[mid] > x:
                r = mid - 1
            
            else:
                l = mid + 1 
        
        return [left_most, right_most]


#{ 
 # Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ob = Solution()
    ans=ob.find(arr,n,x)
    print(*ans)
# } Driver Code Ends