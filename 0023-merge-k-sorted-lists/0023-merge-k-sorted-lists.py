# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge_2_lists(p1, p2):
            dummy = ListNode(0, None)
            curr = dummy
            while p1 or p2:
                val1 = p1.val if p1 else float('inf')
                val2 = p2.val if p2 else float('inf')

                if val1 < val2:
                    curr.next = p1
                    p1 = p1.next
                else:
                    curr.next = p2
                    p2 = p2.next

                curr = curr.next

            return dummy.next
        
        if not lists:
            return None
        if len(lists) == 0:
            return lists[0]
        
        for i in range(1, len(lists)):
            lists[i] = merge_2_lists(lists[i - 1], lists[i])
        
        return lists[len(lists) - 1]