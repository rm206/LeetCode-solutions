#User function Template for python3

from typing import List

class Solution:
    def reverse(self,st): 
        
        def insertAtBottom(st, elt):
            if len(st) == 0:
                st.append(elt)
                return
            
            num = st[-1]
            st.pop()
            insertAtBottom(st, elt)
            st.append(num)
        
        def reverseStack(st):
            if len(st) == 0:
                return
            
            num = st[-1]
            st.pop()
            reverseStack(st)
            insertAtBottom(st, num)
        
        reverseStack(st)
        return st


#{ 
 # Driver Code Starts
#Initial Template for Python 3

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            ans=(ob.reverse(arr))
            for el in ans:
                print(el,end=" ")
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends