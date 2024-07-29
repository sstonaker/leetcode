# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        ptr1 = head
        ptr2 = head.next
        last = head.val
        while ptr2:
            if ptr2.val == last:
                ptr2 = ptr2.next
                ptr1.next = ptr2
            else:
                ptr1 = ptr2
                last = ptr1.val
                ptr2 = ptr2.next
        return head