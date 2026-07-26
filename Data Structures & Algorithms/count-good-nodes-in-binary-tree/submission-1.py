# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def is_good_node(self, node, maxValue):
        if not node:
            return 0
        
        res = 1 if node.val >= maxValue else 0
        maxValue = max(node.val, maxValue)
        res += self.is_good_node(node.left, maxValue)
        res += self.is_good_node(node.right, maxValue)
        return res


    def goodNodes(self, root: TreeNode) -> int:
        return self.is_good_node(root, float('-inf'))
        