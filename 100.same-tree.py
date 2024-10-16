# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_arr = []
        q_arr = []

        def dfs(node, arr):
            if not node:
                arr.append(None)
                return
            else:
                arr.append(node.val)
            dfs(node.left, arr)
            dfs(node.right, arr)

        dfs(p, p_arr)
        dfs(q, q_arr)
        return p_arr == q_arr