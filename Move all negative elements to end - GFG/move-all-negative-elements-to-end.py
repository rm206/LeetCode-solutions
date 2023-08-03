#User function Template for python3

class Solution:
    def segregateElements(self, arr, n):
        # Your code goes here
        pos = []
        neg = []
        
        for i in arr:
            if i >= 0:
                pos.append(i)
            else:
                neg.append(i)
        
        i = 0
        while i < len(pos):
            arr[i] = pos[i]
            i += 1
        
        j = 0
        while i < n:
            arr[i] = neg[j]
            i += 1
            j += 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        ob.segregateElements(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends