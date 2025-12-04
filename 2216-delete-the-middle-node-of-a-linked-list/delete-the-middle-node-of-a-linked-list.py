# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:    return None
        if not head.next:   return None

        prev = slow = fast = ListNode(next=head)

        while fast:
            fast = fast.next
            pre = slow
            slow = slow.next

            if not fast:    break
            fast = fast.next
        

        pre.next = slow.next
        return head
        