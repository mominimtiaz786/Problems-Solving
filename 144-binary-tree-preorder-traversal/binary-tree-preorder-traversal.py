# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal_i(self, root: Optional[TreeNode]) -> List[int]:
        if not root:    return []

        # return [root.val]+self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

        traversal = []
        curr = root
        stack = []

        while curr or stack:
            if curr:
                traversal.append(curr.val)

                if curr.right:
                    stack.append(curr.right)
                curr = curr.left
            
            else:
                curr = stack.pop()
        
        return traversal


    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversal = []
        curr = root

        while curr:
            traversal.append(curr.val)
            
            if not curr.left:
                curr = curr.right
            
            else:
                pred = curr.left
                while pred.right:
                    pred = pred.right
                

                pred.right = curr.right
                curr = curr.left


        return traversal

