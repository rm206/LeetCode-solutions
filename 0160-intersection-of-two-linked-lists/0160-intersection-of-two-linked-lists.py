# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        t1, t2 = headA, headB

        while t1 != t2:
            t1 = t1.next
            t2 = t2.next

            if t1 == t2:
                return t1
            
            if not t1:
                t1 = headB
            if not t2:
                t2 = headA
        
        return t1