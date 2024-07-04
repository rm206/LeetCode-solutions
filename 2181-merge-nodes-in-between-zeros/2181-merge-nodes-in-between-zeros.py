# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        curr = head

        while curr:
            if curr.val == 0 and curr.next:
                between = curr.next
                curr_sum = 0
                while between.val != 0:
                    curr_sum += between.val
                    between = between.next
                curr.next = ListNode(curr_sum, between)
                curr = between
            else:
                curr = curr.next
        
        curr = dummy
        while curr and curr.next:
            if curr.next.val == 0:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next