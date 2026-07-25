# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def merge_two_lists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1

        dummy_node = ListNode()
        dummy_node_head = dummy_node
        while l1 or l2:
            if not l1:
                dummy_node.next = l2
                break
            if not l2:
                dummy_node.next = l1

                break
            if l1.val <= l2.val:
                dummy_node.next = l1
                l1 = l1.next
            else:
                dummy_node.next = l2
                l2 = l2.next
            dummy_node = dummy_node.next

        return dummy_node_head.next

    def merge_helper(self, lists, start, end):
        if start == end:
            return lists[start]

        if start + 1 == end:
            return self.merge_two_lists(lists[start], lists[end])

        mid = (start + end) // 2
        left = self.merge_helper(lists, start, mid)
        right = self.merge_helper(lists, mid + 1, end)
        return self.merge_two_lists(left, right)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        return self.merge_helper(lists, 0, len(lists) - 1)
