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
        
        temp = ListNode()
        curr = temp
        heap = []
        ctr = 0

        for l in lists:
            if l:
                heapq.heappush(heap, [l.val, ctr, l])
                ctr += 1
        
        if not heap:
            return None
        
        while heap:
            val, _, node = heapq.heappop(heap)
            next_to_insert = node.next
            curr.next = node
            curr = curr.next
            if next_to_insert:
                heapq.heappush(heap, [next_to_insert.val, ctr, next_to_insert])
            ctr += 1
        
        return temp.next