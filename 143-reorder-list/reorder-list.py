# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        first = second = head
        while second and second.next:
            first = first.next
            second = second.next.next

        second_half = first.next
        first.next = None

        prev = None
        curr = second_half
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        second_half = prev

        curr = head
        while second_half:
            tmp = curr.next
            curr.next = second_half
            second_half = second_half.next
            curr.next.next = tmp
            curr = tmp