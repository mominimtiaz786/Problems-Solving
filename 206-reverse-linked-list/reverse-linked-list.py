# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:    return head
        if not head.next:   return head


        prev, curr, nex = None, head, head.next

        while nex:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr=nex

        
        return prev

        