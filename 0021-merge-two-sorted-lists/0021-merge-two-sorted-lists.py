# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        c1, c2 = list1, list2

        while c1 or c2:
            v1 = c1.val if c1 else math.inf
            v2 = c2.val if c2 else math.inf

            if v1 < v2:
                curr.next = c1
                c1 = c1.next
            else:
                curr.next = c2
                c2 = c2.next
            
            curr = curr.next
        
        return dummy.next