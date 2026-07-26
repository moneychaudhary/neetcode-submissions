# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def is_identical(self, p, q):
        if not p and not q:
            return True
        if p and not q:
            return False
        if q and not p:
            return False

        return p.val == q.val and self.is_identical(p.left, q.left) and self.is_identical(p.right, q.right)
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        if not root:
            return False
        
        if self.is_identical(root, subRoot):
            return True

        if self.isSubtree(root.left, subRoot):
            return True
        
        if self.isSubtree(root.right, subRoot):
            return True

        return False
        
        