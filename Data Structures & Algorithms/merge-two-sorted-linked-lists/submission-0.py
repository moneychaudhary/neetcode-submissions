# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result_node = ListNode(float('-inf'))
        head = result_node

        while list1 and list2:
            if list1.val <= list2.val:
                result_node.next = list1
                list1 = list1.next
            else:
                result_node.next = list2
                list2 = list2.next
            result_node = result_node.next
        
        if list1:
            result_node.next = list1
        
        if list2:
            result_node.next = list2
        
        return head.next

        

