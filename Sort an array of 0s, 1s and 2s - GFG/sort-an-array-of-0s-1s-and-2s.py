#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        red, white, blue = 0, 0, n - 1
        
        while white <= blue:
            if arr[white] == 1:
                white += 1
            elif arr[white] == 0:
                arr[white], arr[red] = arr[red], arr[white]
                white += 1
                red += 1
            else:
                arr[white], arr[blue] = arr[blue], arr[white]
                blue -= 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends