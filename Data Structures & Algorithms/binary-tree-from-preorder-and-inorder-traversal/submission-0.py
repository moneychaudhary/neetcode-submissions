# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0

        def build_tree(left, right):
            if left > right:
                return None
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            node = TreeNode(root_val)

            mid = inorder_index[root_val]
            node.left = build_tree(left, mid - 1)
            node.right = build_tree(mid + 1, right)
            return node

        return build_tree(0, len(preorder) - 1)
