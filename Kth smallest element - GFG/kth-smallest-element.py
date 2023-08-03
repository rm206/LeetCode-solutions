#User function Template for python3
import heapq
class Solution:
    def kthSmallest(self,arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        '''
        heapq.heapify(arr)
        
        while k:
            val = heapq.heappop(arr)
            if k == 1:
                return val
            
            k -= 1
        '''
        
        max_heap = []
        
        for i in range(k):
            heapq.heappush(max_heap, -1 * arr[i])
        
        i = k
        while i < len(arr):
            if arr[i] < -1 * max_heap[0]:
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, -1 * arr[i])
            
            i += 1
        
        return -1 * max_heap[0]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    import random 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=list(map(int,input().strip().split()))
        k=int(input())
        ob=Solution()
        print(ob.kthSmallest(arr, 0, n-1, k))
        
# } Driver Code Ends