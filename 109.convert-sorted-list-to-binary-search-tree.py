# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructBST(self, left_head: ListNode, right_head: ListNode) -> TreeNode:
        if left_head == right_head:
            return None
        slow, fast = left_head, left_head
        while fast != right_head and fast.next != right_head:
            slow = slow.next
            fast = fast.next.next
        root = TreeNode(slow.val)
        root.left = self.constructBST(left_head, slow)
        root.right = self.constructBST(slow.next, right_head)
        return root

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        if not head.next:
            root = TreeNode(head.val)
            return root
        return self.constructBST(head, None)
