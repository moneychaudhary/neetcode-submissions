# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l2:
            return l1

        if not l1:
            return l2

        carry = 0
        dummy_node = ListNode()
        sum_head = dummy_node
        while l1 or l2:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next

            if total > 9:
                carry = total // 10
                total = total % 10
            else:
                carry = 0

            dummy_node.next = ListNode(total)
            dummy_node = dummy_node.next

        if carry:
            dummy_node.next = ListNode(carry)

        return sum_head.next
