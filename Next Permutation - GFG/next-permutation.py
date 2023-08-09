#User function Template for python3

class Solution:
    def nextPermutation(self, N, arr):
        # code here
        break_point = -1
        
        for i in range(N - 2, -1, -1):
            if arr[i] < arr[i + 1]:
                break_point = i
                break
        
        if break_point == -1:
            arr.reverse()
            return arr
        
        for i in range(N - 1, break_point - 1, -1):
            if arr[i] > arr[break_point]:
                arr[i], arr[break_point] = arr[break_point], arr[i]
                break
        
        temp = arr[break_point + 1 : ]
        temp.reverse()
        arr = arr[:break_point + 1] + temp
        
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        ans = ob.nextPermutation(N, arr)
        for i in range(N):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends