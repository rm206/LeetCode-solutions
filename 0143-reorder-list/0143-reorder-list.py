# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next

        l1, l2 = None, None
        if count % 2 == 0:
            count = count /2
        else:
            count = (count // 2) + 1
        
        l1 = head
        temp = head
        splitCount = 0
        while splitCount < count-1:
            temp = temp.next
            splitCount += 1
            
        l2 = temp.next
        temp.next = None
        l2 = self.reverseList(l2)
        
        dummy = ListNode()
        tail = dummy
        nextL = 1
        while l1 or l2:
            if nextL == 1:
                tail.next = l1
                l1 = l1.next
                nextL = 2
            else:
                tail.next = l2
                l2 = l2.next
                nextL = 1
            tail = tail.next
        
        head = dummy.next
        
                