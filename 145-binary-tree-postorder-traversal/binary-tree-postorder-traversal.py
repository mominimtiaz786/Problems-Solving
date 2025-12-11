# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # recursive
    def postorderTraversal_recursive(self, root: Optional[TreeNode]) -> List[int]:
        if not root:    return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
    

    # iterative
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:    return []

        traversal = []
        stack = [root]
        last = None

        while stack:
            
            if stack[-1].left == stack[-1].right ==  None:
                last = stack.pop()
                traversal.append(last.val)

            elif last and last in [stack[-1].left, stack[-1].right]:
                last = stack.pop()
                traversal.append(last.val)

            
            else:
                curr = stack[-1]
                if curr.right:
                    stack.append(curr.right)
                
                if curr.left:
                    stack.append(curr.left)

                

        return traversal



    # Morris
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