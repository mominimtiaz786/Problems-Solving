# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # pA = headA
        # pB = headB
        # while pA != pB:
        #     if pA:  pA = pA.next
        #     else:   pA = headB

        #     if pB:  pB = pB.next
        #     else:   pB = headA
        
        # return pA

        pA, pB = ListNode(0), ListNode(0)
        pA.next, pB.next = headA, headB

        my_set = set()
        while pA.next:
            my_set.add(pA.next)
            pA = pA.next
        
        while pB.next:
            if pB.next in my_set:
                return pB.next
            pB = pB.next
        
        return None