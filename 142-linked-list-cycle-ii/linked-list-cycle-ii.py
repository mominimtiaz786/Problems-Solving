# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:    return head
        slow = fast = head

        while fast:
            slow = slow.next
            fast = fast.next.next if fast.next else fast.next
            if slow == fast:    break

        if not fast:    return fast

        slow = head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow