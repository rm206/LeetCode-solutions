#User function Template for python3

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    #Function to return the maximum sum of non-adjacent nodes.
    def getMaxSum(self,root):
        def helper(node):
            if not node:
                return [0, 0]
            
            left, right = helper(node.left), helper(node.right)
            
            # first is if including node on current level, second if excluding current level
            ans = [0, 0]
            ans[0] = node.data + left[1] + right[1]
            ans[1] = max(left[0], left[1]) + max(right[0], right[1])
            
            return ans
        
        
        res = helper(root)
        return max(res[0], res[1])


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
import sys
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(10**6)

class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
        
# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__ == '__main__':
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        ob = Solution()
        print(ob.getMaxSum(root))
        
# } Driver Code Ends