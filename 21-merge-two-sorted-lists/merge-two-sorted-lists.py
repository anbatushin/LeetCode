# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            head = list1
            tmp = list2
        else:
            head = list2
            tmp = list1

        curr = head
        while curr and curr.next and tmp:
            if tmp.val <= curr.next.val:
                next = curr.next
                curr.next = tmp
                tmp = tmp.next
                curr.next.next = next
            else:
                curr = curr.next
        if tmp:
            curr.next = tmp
        
        return head

