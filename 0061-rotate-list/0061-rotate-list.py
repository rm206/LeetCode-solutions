# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        curr = head
        l = 1
        while curr.next:
            l += 1
            curr = curr.next

        k = k % l
        if k == 0:
            return head
        
        curr.next = head
        
        curr = head
        ctr = 0
        while ctr < (l-k-1):
            ctr += 1
            curr = curr.next
        
        head = curr.next
        curr.next = None
        return head