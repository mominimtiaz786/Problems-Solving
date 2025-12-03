# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:   return head

        starting_node = ListNode(next=head)

        prev, curr = starting_node, head

        pos = 1
        while pos<left:
            prev = prev.next
            curr = curr.next
            pos+=1
        

        left_node = prev
        prev = prev.next
        curr = curr.next

        pos+=1

        while pos <= right:
            tmp = curr.next

            curr.next = prev
            prev = curr
            curr = tmp
            pos+=1
        
        left_node.next.next = curr
        left_node.next = prev

        return starting_node.next





            

