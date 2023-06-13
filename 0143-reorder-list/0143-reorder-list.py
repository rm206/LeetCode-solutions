# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def reverseList(head):
            prev, curr = None, head

            while curr:
                next_temp = curr.next
                curr.next = prev
                prev = curr
                curr = next_temp

            return prev
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        r_head = slow.next
        slow.next = None
        r_head = reverseList(r_head)
        
        dummy = ListNode()
        curr = dummy
        p1, p2 = head, r_head
        turn = 1
        
        while p1 or p2:
            if turn == 1:
                curr.next = p1
                curr = curr.next
                p1 = p1.next
                turn *= -1
            else:
                curr.next = p2
                curr = curr.next
                p2 = p2.next
                turn *= -1

        
        head = dummy.next