# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a


    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:    return head
        if not head.next:   return head

        curr, nex = head, head.next

        while nex:
            divisor = math.gcd(curr.val, nex.val)

            tmp = ListNode(val=divisor, next=nex)
            curr.next = tmp

            curr = nex
            nex = nex.next
        

        return head
