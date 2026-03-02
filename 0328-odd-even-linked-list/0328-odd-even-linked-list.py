# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_head, even_head = ListNode(-1), ListNode(-1)
        curr = head
        odd_curr, even_curr = odd_head, even_head

        flag = 1
        while curr:
            next_curr = curr.next

            if flag == 1:
                odd_curr.next = curr
                odd_curr = odd_curr.next
                odd_curr.next = None
            if flag == -1:
                even_curr.next = curr
                even_curr = even_curr.next
                even_curr.next = None
            
            # curr = curr.next
            curr = next_curr
            flag *= -1
        
        # even_curr.next = None
        odd_curr.next = even_head.next

        return odd_head.next