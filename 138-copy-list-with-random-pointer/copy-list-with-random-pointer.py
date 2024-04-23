"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    set_list = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        head = head
        if head in self.set_list:
            return self.set_list[head]

        new = Node(head.val)
        self.set_list[head] = new
        new.next = self.copyRandomList(head.next)
        new.random = self.copyRandomList(head.random)

        return new