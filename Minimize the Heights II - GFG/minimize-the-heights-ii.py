#User function Template for python3

class Solution:
    def getMinDiff(self, arr, n, k):
        
        arr.sort()
        
        big, small = arr[-1], arr[0]
        diff = big - small
        
        for i in range(n - 1):
            if arr[i + 1] < k:
                continue
            
            maxi = max(big - k, arr[i] + k)
            mini = min(small + k, arr[i + 1] - k)
            
            diff = min(diff, maxi - mini)
        
        return diff

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends