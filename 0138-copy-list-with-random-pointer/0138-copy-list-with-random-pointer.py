"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        s = {}
        s[None] = None
        
        ptr = head
        while ptr:
            s[ptr] = Node(ptr.val, None, None)
            ptr = ptr.next
        
        ptr = head
        while ptr:
            s[ptr].next = s[ptr.next]
            s[ptr].random = s[ptr.random]
            ptr = ptr.next
        
        return s[head]