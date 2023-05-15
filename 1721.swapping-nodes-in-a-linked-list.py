# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        length = 1
        while cur.next:
            length += 1
            cur = cur.next

        cur = head
        for i in range(1, length + 1):
            if i == k:
                swap1 = cur
            if i == length + 1 - k:
                swap2 = cur
            cur = cur.next

        swap1.val, swap2.val = swap2.val, swap1.val

        return head
