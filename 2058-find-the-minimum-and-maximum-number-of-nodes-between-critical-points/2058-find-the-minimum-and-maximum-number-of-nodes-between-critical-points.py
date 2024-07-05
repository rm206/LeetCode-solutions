# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        res = [-1, -1]
        if not head.next.next:
            return res
        
        curr = head.next
        prev = head
        positions = []
        pos = 1
        poses_appended = 0

        while curr:
            if curr.next:
                if (prev.val < curr.val and curr.val > curr.next.val) or (prev.val > curr.val and curr.val < curr.next.val):
                    positions.append(pos)
                    poses_appended += 1
            pos += 1
            prev = prev.next
            curr = curr.next
        
        if poses_appended < 2:
            return res

        res[0], res[1] = positions[-1] - positions[0], positions[-1] - positions[0]

        if poses_appended == 2:
            return res
        
        i = 1
        while i < poses_appended:
            res[0] = min(positions[i] - positions[i - 1], res[0])
            i += 1

        return res