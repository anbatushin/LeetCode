# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        set_list = set()

        curr = head
        while curr:
            if curr in set_list:
                return True
            else:
                set_list.add(curr)
                curr = curr.next
    
        return False