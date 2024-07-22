# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0:
            return head
        
        if not head or (not head.next):
            return head
        
        ll = 0
        prev = None
        temp = head
        while temp:
            prev = temp
            temp = temp.next
            ll += 1
        
        prev.next = head
        k = k % ll
        cnt = 1
        curr = head
        while cnt < ll - k:
            curr = curr.next
            cnt += 1
        
        new_head = curr.next
        curr.next = None

        return new_head