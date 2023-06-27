import collections

class Solution:
    def diagonal(self,root):
        res = []
        
        if not root:
            return res
        
        def helper(node, hd):
            if not node:
                return
            
            mapping[hd].append(node.data)
            
            helper(node.left, hd - 1)
            helper(node.right, hd)
        
        mapping = collections.defaultdict(list)
        helper(root, 0)
        min_hd = min(mapping.keys())
        for i in range(0, min_hd - 1, -1):
            for j in mapping[i]:
                res.append(j)
        
        return res


'''
        res = []
        
        if not root:
            return res
            
        mapping = collections.defaultdict(list)
        
        q = []
        q.append((root, 0))
        
        while len(q) != 0:
            popped_node, hd = q.pop(0)
            
            mapping[hd].append(popped_node.data)
            
            if popped_node.left:
                q.append((popped_node.left, hd - 1))
            if popped_node.right:
                q.append((popped_node.right, hd))
        
        min_hd = min(mapping.keys())
        for i in range(0, min_hd - 1, -1):
            for j in mapping[i]:
                res.append(j)
        
        return res
'''


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(50000)
#Contributed by Sudarshan Sharma
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

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
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        obj=Solution()
        diagonalNode = obj.diagonal(root)
        for node in diagonalNode:
            print(node,end=' ')
        print()

# } Driver Code Ends