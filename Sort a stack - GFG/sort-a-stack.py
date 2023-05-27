class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def sorted(self, s):
        # Code here
        
        def insert_sorted(s, num):
            if len(s) == 0:
                s.append(num)
                return
            
            if s[-1] <= num:
                s.append(num)
                return
            elt = s[-1]
            s.pop()
            insert_sorted(s, num)
            s.append(elt)
        
        def sort_stack(s):
            # keep top elt aside
            # sort rest of the stack recursively
            # insert top elt in sorted order
            if len(s) == 0:
                return
            
            num = s[-1]
            s.pop()
            sort_stack(s)
            insert_sorted(s, num)
        
        sort_stack(s)


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.sorted(arr)
        for e in range(len(arr)):
            print(arr.pop(), end=" ")
        print()


# } Driver Code Ends