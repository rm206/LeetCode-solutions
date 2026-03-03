# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        heap = []
        ctr = 0

        for l in lists:
            if l:
                heapq.heappush(heap, [l.val, ctr, l])
                ctr += 1
        
        dummy = ListNode(-1)
        curr = dummy

        while heap:
            _, _, node = heapq.heappop(heap)

            curr.next = node
            curr = node

            if node.next:
                heapq.heappush(heap, [node.next.val, ctr, node.next])
                ctr += 1
        
        return dummy.next