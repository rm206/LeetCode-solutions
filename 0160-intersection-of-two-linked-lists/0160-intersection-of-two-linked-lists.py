# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1, l2 = 0, 0

        curr = headA
        while curr:
            l1 += 1
            curr = curr.next
        curr = headB
        while curr:
            l2 += 1
            curr = curr.next
        
        while l1 > l2:
            headA = headA.next
            l1 -= 1
        while l2 > l1:
            headB = headB.next
            l2 -= 1
        
        c1, c2 = headA, headB
        while c1 and c2:
            if c1 == c2:
                return c1
            c1 = c1.next
            c2 = c2.next
        
        return None