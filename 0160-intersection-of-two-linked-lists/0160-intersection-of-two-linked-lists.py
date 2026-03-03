# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node1, node2 = headA, headB

        while node1 != node2:
            node1 = node1.next
            node2 = node2.next

            if node1 == node2:
                return node1
            
            if not node1:
                node1 = headB
            if not node2:
                node2 = headA
            
        return node1