#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        expected_sum = (n * (n + 1)) // 2
        set_sum = sum(set(arr))
        actual_sum = sum(arr)
        
        return [actual_sum - set_sum, expected_sum - set_sum]

'''
s = set()
for i in range(1, n + 1):
    s.add(i)

for i in arr:
    if i not in s:
        A = i
    else:
        s.remove(i)
B = s.pop()

return [A, B]
'''

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends