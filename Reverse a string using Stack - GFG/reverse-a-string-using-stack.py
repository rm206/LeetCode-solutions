#{ 
 # Driver Code Starts

# } Driver Code Ends
def reverse(S):
    
    #Add code here
    stack = []
    for c in S:
        stack.append(c)
    res = ""
    while len(stack) != 0:
        res += stack.pop()
    
    return res
    
    

#{ 
 # Driver Code Starts.
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        print(reverse(str1))
# } Driver Code Ends