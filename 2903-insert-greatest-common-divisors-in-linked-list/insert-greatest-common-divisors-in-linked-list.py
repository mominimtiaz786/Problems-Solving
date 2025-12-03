# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findDivisor(self, n1, n2):
        n1, n2 = (n1, n2) if n1 < n2 else (n2, n1)
        divisor = 1
        for i in range(1, n1+1):
            if n1 % i == 0:
                num = n1//i
                if n2 % num == 0:
                    divisor = num
                    break

        return divisor


    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:    return head
        if not head.next:   return head

        curr, nex = head, head.next

        while nex:
            divisor = self.findDivisor(curr.val, nex.val)

            tmp = ListNode(val=divisor, next=nex)
            curr.next = tmp

            curr = nex
            nex = nex.next
        

        return head
