# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def height(self, root):
        if not root:
            return 0
        
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        return 1 + max(left_height,right_height )

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return max(
            self.height(root.left) + self.height(root.right),
            self.diameterOfBinaryTree(root.left),
            self.diameterOfBinaryTree(root.right),
        )
        