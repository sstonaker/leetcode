# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mirror(tree1: TreeNode, tree2: TreeNode) -> bool:
            if not tree1 and not tree2:
                return True
            if not tree1 or not tree2:
                return False
            return tree1.val == tree2.val and mirror(tree1.left, tree2.right) and mirror(tree2.left, tree1.right)
        return mirror(root, root)
