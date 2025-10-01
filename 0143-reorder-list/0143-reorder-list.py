# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def reverse_list(node):
            prev, curr= None, node
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        
        if not head or not head.next:
            return None
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = None
        second_list = reverse_list(slow)

        temp = ListNode()
        curr = temp
        p1, p2 = head, second_list
        turn = 1

        while p1 and p2:
            if turn == 1:
                curr.next = p1
                p1 = p1.next
            else:
                curr.next = p2
                p2 = p2.next
            turn *= -1
            curr = curr.next
        
        if p1:
            curr.next = p1
        if p2:
            curr.next = p2