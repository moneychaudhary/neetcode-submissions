"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        old_new_mapping = {}
        
        current = head
        while current:
            old_new_mapping[current] = Node(current.val)
            current = current.next

        current = head
        while current:
            old_new_mapping[current].next = old_new_mapping.get(current.next)
            old_new_mapping[current].random = old_new_mapping.get(current.random)
            current = current.next
        
        return old_new_mapping[head]

        