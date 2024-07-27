# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        total_len = 0
        head2 = head
        while head != None:
            total_len += 1
            head = head.next

        if total_len % 2 == 0:
            total_len += 1
        middle = math.ceil(total_len / 2)

        for i in range(1, middle + 1):
            new_head = head2
            head2 = head2.next
        return new_head