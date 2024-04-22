# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        if length == n:
            return head.next

        length -= n - 1
        curr = head
        while length > 2:
            curr = curr.next
            length -= 1

        if n == 1:
            curr.next = None
        else:
            curr.next = curr.next.next
        
        return head