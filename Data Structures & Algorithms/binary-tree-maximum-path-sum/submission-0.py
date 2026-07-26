# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.sum = float("-inf")

        def max_path(node):
            if not node:
                return 0
            left_sum = max(max_path(node.left), 0)
            right_sum = max(max_path(node.right), 0)
            total = node.val + left_sum + right_sum
            self.sum = max(self.sum, total)
            return node.val + max(left_sum, right_sum)

        max_path(root)
        return self.sum
