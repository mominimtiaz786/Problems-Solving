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

    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head:    return True
        if not head.next:   return True

        # O(n) tc and O(1) sc solution
        nodes_count = self.nodesCounter(head)
        

        is_even = (nodes_count % 2 == 0)
        half_count = nodes_count // 2

        first_half = head

        ptr = head
        twin_sums = [0]*half_count
        for i in range(half_count):
            twin_sums[i] = ptr.val
            ptr = ptr.next
        
        for i in range(half_count):
            twin_sums[-(i+1)]+=ptr.val
            ptr = ptr.next

        return max(twin_sums)

        second_half = None
        second_half = ptr.next
        ptr.next = None

        second_half = self.reverseList(second_half)

        ptr1 = first_half
        ptr2 = second_half

        twin_sum = float('-inf')
        while ptr1:
            twin_sum = max(twin_sum, ptr1.val+ptr2.val)
            ptr1 = ptr1.next
            ptr2 = ptr2.next


        return twin_sum
