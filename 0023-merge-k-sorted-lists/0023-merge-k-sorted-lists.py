# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode(-1, None)
        curr = dummy

        cnt = 0
        for l in lists:
            if l:
                heapq.heappush(heap, [l.val, cnt, l])
                cnt += 1
        
        while heap:
            val, c, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, [node.next.val, cnt, node.next])
                cnt += 1
        
        return dummy.next