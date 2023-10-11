
class Solution:
    def trappingWater(self, arr,n):
        #Code here
        l_max = [0 for i in range(n)]
        r_max = [0 for i in range(n)]
        
        l = arr[0]
        for i in range(1, n - 1):
            l = max(l, arr[i])
            l_max[i] = max(l, arr[i])
        
        r = arr[n - 1]
        for i in range(n - 2, 0, -1):
            r = max(r, arr[i])
            r_max[i] = max(r, arr[i])
        
        res = 0
        for i in range(1, n - 1):
            res += max(min(l_max[i], r_max[i]) - arr[i], 0)
        
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends