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

    def nodesCounter(self, head):
        nodes_count = 0
        ptr = head
        while ptr:
            nodes_count+=1
            ptr = ptr.next
        
        return nodes_count


    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:    return True
        if not head.next:   return True

        # O(n) tc and O(1) sc solution
        nodes_count = self.nodesCounter(head)
        

        is_even = (nodes_count % 2 == 0)
        half_count = nodes_count // 2

        first_half = head

        ptr = head
        for i in range(half_count-1):
            ptr = ptr.next

        second_half = None
        if is_even:
            second_half = ptr.next
            ptr.next = None
        else:
            second_half = ptr.next.next
            ptr.next.next = None
            ptr.next = None

        second_half = self.reverseList(second_half)

        ptr1 = first_half
        ptr2 = second_half

        while ptr1:
            if ptr1.val != ptr2.val:
                return False
            ptr1 = ptr1.next
            ptr2 = ptr2.next


        return True





            